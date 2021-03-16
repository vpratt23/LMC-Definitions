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
