import numpy as np
from numpy import random
import scipy.special
from astropy.coordinates import SkyCoord
import astropy.units as u

def cutting_dist(x, distances):
	"""
		creates new dictionary of SAGA-host-keys that link to the distances of all other galaxies that lie within some radius out from the host-key
		
		Args:
			x = maximum distance in Mpc you will allow your galaxies to be apart, the radius 
			shorter = an empty dictionary
			distances = a dictionary of SAGA hosts that catalogs the projected distances of it to every other SAGA host
		
		Returns: dictionary of selections from distances that meet the distance cut

	"""
	shorter = {}
	for galaxy in distances.keys():
		shorter[galaxy] = []
		for i in range(len(distances[galaxy])):
			if distances[galaxy][i][0] <=x:
				shorter[galaxy].append(distances[galaxy][i][0])
	return shorter


def number_galaxies(shorter):
	"""
		creates new dictionary of SAGA-host-keys that link to the number of all galaxies that lie within some radius
		
		Args:
			shorter = the dictionary of distances cut at some value, each SAGA-host-key links to an array of all of the different distances within that value
			num = an empty dictionary
		
		Returns: a dictionary with values of the amount of galaxies within some radius of the keys
	"""
	num = {}
	for key in shorter.keys():
		num[key] = len(shorter[key])
	return num

def number_galaxies_2_param(shorter, hosts, param_a, param_b):
	"""
		creates 2 new dictionaries of SAGA-host-keys that link to the number of all galaxies that lie within some radius, split by whether the hosts follow 		parameter A or parameter b
		
		Args:
			shorter = the dictionary of distances cut at some value, each SAGA-host-key links to an array of all of the different distances within that value
			hosts = a dictionary of the SAGA hosts that equal param_a or param_b
			param_a = some parameter, could be of any type
			param_b = some parameter, could be of any type

		Returns: two dictionaries with values of the amount of galaxies within some radius of the keys; the keys in the two dictionaries are different however, depending on whether the hosts[galaxy] = param_a or param_b
	"""
	num_a = {}
	num_b = {}
	for galaxy in hosts.keys():
		if hosts[galaxy] == param_a:
			num_a[galaxy] = len(shorter[galaxy])
		if hosts[galaxy] == param_b:
			num_b[galaxy] = len(shorter[galaxy])  
	return (num_a, num_b)  

def converting_to_arr(dictionary, arr):
	"""
		takes the values from a dictionary of arrays and combines them into one long array
		useful for taking statistical data across hosts
		
		Args:
			dictionary = whatever dictionary of arrays you want to convert into an array
			arr = an empty array
		
		Returns: an array including your dictionary values for every key
	"""
	arr = []
	for key in dictionary.keys():
		arr.append(dictionary[key])
	return arr

def shorter_dist_lum_cut_range(distance, x, y, z):
	"""
		takes the values from a dictionary of arrays and combines them into one long array
		useful for taking statistical data across hosts
		
		Args:
			distances = dictionary with SAGA-host-keys that links to an array of first the distance from the host and subsequently the luminosity of all the 					other SAGA hosts
			shorter = an empty dictionary
			x = some r-band luminosity
			y = some upper limit on the distance 
			z = some lower limit on the distance

		Returns: dictionary of selections from distances that meet the distance cut and luminosity cut
	"""
	shorter = {}
	for galaxy in distance.keys():
		shorter[galaxy] = []
		for i in range(len(distance[galaxy])):
			if distance[galaxy][i][1] <= x:
				if distance[galaxy][i][0] <=y and distance[galaxy][i][0] >= z:
					shorter[galaxy].append(distance[galaxy][i][0])
	return shorter

def jack_knifing(split, hosts):
	"""
		randomly spits up SAGA hosts into true/false to help determine statistical significance of other data
		
		Args:
			split = empty dictionary
			hosts = some column or array or list of SAGA_host names

		Returns: dictionary with SAGA-host-keys that is randomly true or false
	"""
	split = {}
	for galaxy in hosts:
		rand = random.randint(11)
		if rand%2 ==0:
			split[galaxy] = True
		else: 
			split[galaxy] = False
	return split

