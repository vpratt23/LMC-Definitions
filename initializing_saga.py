#%pip install <https://github.com/sagasurvey/saga/archive/master.zip>

import pickle
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats 

import SAGA
saga = SAGA.QuickStart()
#os.remove(saga.database["host_stats"].local.path)
#saga.database["host_stats"].clear_cache()
hosts = saga.host_catalog.load(include_stats=True)
#assert saga.good.count(hosts) == 136
#assert saga.paper2_complete.count(hosts) == 36
#assert saga.complete.count(hosts) >= 76

from SAGA.database import FitsTable  # needs version >= 0.21.3
from easyquery import Query
from easyquery import QueryMaker

from numpy import random
import numpy as np

saga = SAGA.QuickStart()

hosts = saga.host_catalog.load(include_stats="remote")
completed_hosts = saga.host_catalog.load(query="paper2_complete", include_stats="remote")
observed_hosts = saga.host_catalog.load(query="observed", include_stats="remote")

from SAGA import ObjectCuts as C
#hosts = saga.host_catalog.load(query = "completed", include_stats = True)["HOSTID"]
sats_url = "https://www.dropbox.com/sh/7qeuqkq0c591k2g/AAC0c5C7erNCp0nYOhcDv9kva/saga_sats_latest.fits?dl=1"
sats = FitsTable(sats_url).read()

# To extract satellites from complete hosts
complete_host_query = saga.host_catalog.construct_host_query("paper2_complete")
sats_completed_hosts = complete_host_query.filter(sats)

#observed_host_query = saga.host_catalog.construct_host_query("paper2_observed")
#sats_observed_hosts = complete_host_query.filter(sats)
	
host_sats = {}
completed_hosts_sorted = {}
sats_completed_hosts_sorted = {}

for host in np.unique(sats_completed_hosts['HOSTID']):
    host_sats[host] = len(sats_completed_hosts[np.logical_and(sats_completed_hosts['HOSTID']==host, sats_completed_hosts['Mr']<=12.3)])
    completed_hosts_sorted[host] = completed_hosts[completed_hosts['HOSTID']==host]
    sats_completed_hosts_sorted[host] = sats_completed_hosts[sats_completed_hosts['HOSTID']==host]
    
host_sats = {k: v for k, v in sorted(host_sats.items(), key=lambda item: item[1])} #sort by number of satellites

def load_table(name, including_stats):
    """
        loads in whatever Fits Tables of a set of SAGA hosts and corresponding satellites

        Args: 
            name = string of the name by which you're selecting your hosts
            including_stats = what stats are being included in the table

        Returns: 2 Fits Tables, one of the set of hosts and the other of the set of their satellites
    """

    table = saga.host_catalog.load(query=name, include_stats=including_stats)
    table_query = saga.host_catalog.construct_host_query(name)
    sats_table = complete_host_query.filter(sats)
    return table, sats_table

def sort_table(table, sats_table):
     """
        sorts through whatever tables of hosts and satellites with the hosts as their keys

        Args: 
            table = a Fits Table of SAGA hosts
            sats_table = a Fits Table of corresponding SAGA satellites

        Returns: 2 dictionaries with same-ordered keys of SAGA host names
    """
    table_hosts_sorted
    for host in np.unique(sats_table['HOSTID']):
        table_hosts_sorted[host] = table[table['HOSTID']==host]
        sats_table_sorted[host] = sats_table[sats_table['HOSTID']==host]
    
    return table_hosts_sorted, sats_table_sorted
    

   

