import numpy as np
from initializing_saga import completed_hosts_sorted, sats_completed_hosts_sorted, completed_hosts

hosts_with_LMCs = {}
for key in completed_hosts['HOSTID']:
	if key in sats_completed_hosts_sorted.keys():
		if np.min(sats_completed_hosts_sorted[key]['Mr'])<-18.3:
			hosts_with_LMCs[key] = True
		else: 
			hosts_with_LMCs[key] = False
	else:
		hosts_with_LMCs[key] = False
#magnitude gap between host/brightest satellite
magnitude_gap_hs = {}
for key in sats_completed_hosts_sorted.keys():
    x = list(completed_hosts_sorted.keys()).index(key)
    if len(sats_completed_hosts_sorted[key])>0:
        min_mag = np.sort(sats_completed_hosts_sorted[key]['Mr'])[0]
        host_mag = completed_hosts_sorted[key]['K_ABS'][0]
        magnitude_gap_hs[key] = host_mag-min_mag
    else: magnitude_gap_hs[key] = 0

magnitude_gap_sat = {}
for key in sats_completed_hosts_sorted.keys():
    if len(sats_completed_hosts_sorted[key])>1:
        sats_sorted = sorted(sats_completed_hosts_sorted[key]['Mr'])
        min_mag = sats_sorted[0]
        sec_min_mag = sats_sorted[1]
        magnitude_gap_sat[key] = min_mag-sec_min_mag
    else: magnitude_gap_sat[key] = 0

def determining_LMCs(table, column, sorted_dictionary_satellites, Mr):
	"""
		determines whether hosts have an LMC analog based on luminosity
		
		Args:
			table = table of SAGA hosts
			column =  string name of column of data within the table to sort by
			sorted_dictionary_satellites = dictionary of satellites sorted by said column, contains all the luminosity data about the satellites
			Mr = the luminosity in the r-band at which a satellite is an LMC
		
		Returns: dictionary of True/False depending on whether SAGA host contains LMC

	"""
	hosts_LMCs = {}
	for key in table[column]:
		if key in sorted_dictionary_satellites.keys():
			if np.min(sorted_dictionary_satellites[key]["Mr"]) < Mr:
				hosts_LMCs[key] = True
			else:  
				hosts_LMCs[key] = True
		else:
			hosts_LMCs[key] = False
	return hosts_LMCs

def magnitude_gap_host_sat(sorted_dictionary_satellites, index_choice, sorted_dictionary_hosts):
	"""
		calculates magnitude gap between the host and one of it’s satellites 
		
		Args:
			sorted_dictionary_satellites = dictionary of satellites sorted by ‘HOSTID’, contains all the luminosity data about the satellites
			sorted_dictionary_hosts = dictionary of hosts sorted by ‘HOSTID’, contains all the luminosity data about the hosts
			index_choice = satellite you want to look at
		Returns: dictionary of values of luminosity gap between the host-key and it’s satellite

	"""
	mag_gap = {}
	for key in sorted_dictionary_satellites.keys():
		if len(sorted_dictionary_satellites[key])>0:
			min_mag = np.sort(sorted_dictionary_satellites[key]["Mr"])[index_choice]
			host_mag = sorted_dictionary_hosts[key]["K_ABS"][0]
			mag_gap[key] = host_mag-min_mag
		else: 
			mag_gap[key] = 0
	return mag_gap
  
def magnitude_gap_sat_sat(sorted_dictionary_satellites, index1, index2):
	"""
		calculates magnitude gap between two satellites of 1 host 
		
		Args:
			sorted_dictionary_satellites = dictionary of satellites sorted by ‘HOSTID’, contains all the luminosity data about the satellites
			index1 = first satellite you want to look at
			index2 = second satellite you want to look at
		Returns: dictionary of values of luminosity gap between a satellite and another satellite

	"""
	mag_gap = {}
	for key in sorted_dictionary_satellites.keys():
		if len(sorted_dictionary_satellites[key])>1:
			sats_sorted = sorted(sorted_dictionary_satellites[key]["Mr"])
			min_mag = sats_sorted[index1]
			sec_min_mag = sats_sorted[index2]
			mag_gap[key] = min_mag-sec_min_mag
		else: 
			mag_gap[key] = 0
	return mag_gap
