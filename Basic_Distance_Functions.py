from astropy.coordinates import SkyCoord
import astropy.units as u
import numpy as np
#environmental_master_list = pd.read_csv(r'/Users/Veronica/Downloads/Summer_2020_research/master_list_v2.csv')

def get_dists(ra1,ra2, dec1, dec2, dist1, dist2):
	"""
		calculates projected distances between 2 celestial objects, returns the distance in Mpc
		
		Args:
			ra1/ra2 = objects’ right ascensions, can be found in master_list_v2.csv
			dec1/dec2 = objects’ declinations, can be found in master_list_v2.csv
			dist1/dist2 = objects’ distance from us, can be found in master_list_v2.csv 
		
		Returns: a projected distance value
		
	"""
	c1 = SkyCoord(ra = ra1*u.deg,dec=dec1*u.deg,distance=dist1*u.mpc)
	c2 = SkyCoord(ra=ra2*u.deg,dec=dec2*u.deg,distance=dist2*u.mpc)
	indices = np.argsort(np.abs(c1.cartesian.get_xyz().value))
	xdist = (c1.cartesian.get_xyz().value[indices][0]-c2.cartesian.get_xyz().value[indices][0])**2
	ydist = (c1.cartesian.get_xyz().value[indices][1]-c2.cartesian.get_xyz().value[indices][1])**2
	dist = np.sqrt(xdist+ydist)
	return dist

def dist_galaxies(table, column, environmental_master_list):
	"""
		uses the method get_dists on SAGA galaxies and data
		
		Args:
			table = some FitsTable of SAGA elements
			column = ‘HostID’ most likely, or whatever column you want to index your table and environmental list by
			environmental_master_list = ideally master_list_v2.csv, or some other catalog of data including right ascensions, declinations, and distances from Earth for celestial objects (other galaxies)

		Returns: dictionary with SAGA-host-keys linked to the host’s distance to each of the other celestial objects (other galaxies) in your environmental_master_list		
	"""
	distance_galaxies = {}
	for galaxy in table[column]:
		distance_galaxies[galaxy] = []
		index = environmental_master_list[environmental_master_list[column] == galaxy].index.values[0]
		for j in range(len(environmental_master_list)):
			gal = environmental_master_list[column][j]
			x = 0
			if j != index:
				galaxy1 = environmental_master_list.loc[environmental_master_list[column] == galaxy]
				ra1 = galaxy1['RA'].values[0]
				dec1 = galaxy1['DEC'].values[0]
				dist1 = galaxy1['DIST'].values[0]
				galaxy2 = environmental_master_list.loc[environmental_master_list[column] == gal]
				ra2 = galaxy2['RA'].values[0]
				dec2 = galaxy2['DEC'].values[0]
				dist2 = galaxy2['DIST'].values[0]
				dist = get_dists(ra1,ra2, dec1, dec2, dist1, dist2)
				distance_galaxies[galaxy].append((dist, galaxy2['K_ABS'].values[0]))
	return distance_galaxies