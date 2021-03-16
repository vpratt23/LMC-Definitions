##Pre-computed catalogs for halos matched to SAGA hosts
import pickle
import numpy as np
import SAGA
from SAGA.database import FitsTable
from easyquery import Query
from easyquery import QueryMaker

saga = SAGA.QuickStart()
hosts = saga.host_catalog.load(include_stats=True)
completed_hosts = saga.host_catalog.load(query="paper2_complete", include_stats="remote")
df_completed_hosts = completed_hosts.to_pandas()

with open(r'sat.pickle', 'rb') as f:
    sat = pickle.load(f, encoding='latin1')

with open(r'host_halo.pickle', 'rb') as f:
    host_halo = pickle.load(f, encoding='latin1')
    
with open(r'rproj.pickle', 'rb') as f:
    rproj = pickle.load(f, encoding='latin1')
    
with open(r'vproj.pickle', 'rb') as f:
    vproj = pickle.load(f, encoding='latin1')
    
with open(r'Mr.pickle', 'rb') as f:
    Mr = pickle.load(f, encoding='latin1')

#Pre-computed catalogs for halos matched to SAGA hosts
with open(r"sat_01dex.pickle", "rb") as f:
    sat_01 = pickle.load(f, encoding='latin1')
    
with open(r"host_halo_01.pickle", "rb") as f:
    host_halo_01 = pickle.load(f, encoding='latin1')
    
with open(r"rproj_01.pickle", "rb") as f:
    rproj_01 = pickle.load(f, encoding='latin1')
    
with open(r"vproj_01.pickle", "rb") as f:
    vproj_01 = pickle.load(f, encoding='latin1')
    
with open(r"Mr_01.pickle", "rb") as f:
    Mr_01 = pickle.load(f, encoding='latin1')

#Pre-computed catalogs for halos matched to SAGA hosts
with open(r"sat_02dex.pickle", "rb") as f:
    sat_02 = pickle.load(f, encoding='latin1')
    
with open(r"host_halo_02.pickle", "rb") as f:
    host_halo_02 = pickle.load(f, encoding='latin1')
    
with open(r"rproj_02.pickle", "rb") as f:
    rproj_02 = pickle.load(f, encoding='latin1')
    
with open(r"vproj_02.pickle", "rb") as f:
    vproj_02 = pickle.load(f, encoding='latin1')
    
with open(r"Mr_02.pickle", "rb") as f:
    Mr_02 = pickle.load(f, encoding='latin1')


def actual_Mr_for_sats(Mrex, sigma_M_sat):
    x = {}
    for host in Mrex.keys():
        if len(Mrex[host])>0:
            x[host] = []
            for i in range(len(Mrex[host])):
                x[host].append(draw_Mr_simple(Mrex[host][i], sigma_M_sat))
    return x

Mr_015_real = actual_Mr_for_sats(Mr, 0.15)
Mr_01_real = actual_Mr_for_sats(Mr_01, 0.1)
Mr_02_real = actual_Mr_for_sats(Mr_02, 0.2)

def predicting_sat_Mr(satex, Mrex):
    x = {}
    for key in satex.keys():
        x[key] = []
        for i in range(len(satex[key])):
            x[key].append(Mrex[key][i][Mrex[key][i]<-12.3])
    return x

pred_015_sat_MR = predicting_sat_Mr(sat, Mr_015_real)
pred_01_sat_MR = predicting_sat_Mr(sat, Mr_01_real)
pred_02_sat_MR = predicting_sat_Mr(sat, Mr_02_real)

def predicting_LMCs(satex, Mrex):
    x = {}
    for key in satex.keys():
        x[key] = []
        for i in range(len(satex[key])):
            x[key].append(len(Mrex[key][i][Mrex[key][i]<-18.3]))
    return x

pred_LMC_015 = (sat, Mr_015_real)
pred_01_LMC= (sat, Mr_01_real)
pred_02_LMC = (sat, Mr_02_real)

chance_of_LMC_015 = {}
for key in pred_LMC_015.keys():
    tot = 0
    for i in range(len(pred_LMC_015[key])):
        if pred_LMC_015[key][i]>0:
            tot = tot +1
    chance_of_LMC_015[key] = tot/len(pred_LMC_015[key])
chance_LMC_015_arr = []
for key in chance_of_LMC_015.keys():
    chance_LMC_015_arr.append(chance_of_LMC_015[key])

chance_of_LMC_01 = {}
for key in pred_01_LMC.keys():
    tot = 0
    for i in range(len(pred_01_LMC[key])):
        if pred_01_LMC[key][i]>0:
            tot = tot +1
    chance_of_LMC_01[key] = tot/len(pred_01_LMC[key])
chance_LMC_01_arr = []
for key in chance_of_LMC_01.keys():
    chance_LMC_01_arr.append(chance_of_LMC_01[key])

chance_of_LMC_02 = {}
for key in pred_02_LMC.keys():
    tot = 0
    for i in range(len(pred_02_LMC[key])):
        if pred_02_LMC[key][i]>0:
            tot = tot +1
    chance_of_LMC_02[key] = tot/len(pred_02_LMC[key])
chance_LMC_02_arr = []
for key in chance_of_LMC_02.keys():
    chance_LMC_02_arr.append(chance_of_LMC_02[key])

pred_01_mag_gap = {}
for host in pred_01_sat_MR.keys():
    pred_01_mag_gap[host] = []
    if host in completed_hosts['HOSTID']:
        index = df_completed_hosts[df_completed_hosts['HOSTID'] == host].index.values
        mr_host = completed_hosts['K_ABS'][index][0]
    for i in range(len(pred_01_sat_MR[host])):
        if len(pred_01_sat_MR[host][i]) > 0:
            mr_bright_sat = np.min(pred_01_sat_MR[host][i])
            pred_01_mag_gap[host].append(mr_host-mr_bright_sat)
        else: 
            pred_01_mag_gap[host].append(-15)

pred_02_mag_gap = {}
for host in pred_02_sat_MR.keys():
    pred_02_mag_gap[host] = []
    if host in completed_hosts['HOSTID']:
        index = df_completed_hosts[df_completed_hosts['HOSTID'] == host].index.values
        mr_host = completed_hosts['K_ABS'][index][0]
    for i in range(len(pred_02_sat_MR[host])):
        if len(pred_02_sat_MR[host][i]) > 0:
            mr_bright_sat = np.min(pred_02_sat_MR[host][i])
            pred_02_mag_gap[host].append(mr_host-mr_bright_sat)
        else: 
            pred_02_mag_gap[host].append(-15)

pred_015_mag_gap = {}
for host in pred_015_sat_MR.keys():
    pred_015_mag_gap[host] = []
    if host in completed_hosts['HOSTID']:
        index = df_completed_hosts[df_completed_hosts['HOSTID'] == host].index.values
        mr_host = completed_hosts['K_ABS'][index][0]
    for i in range(len(pred_015_sat_MR[host])):
        if len(pred_015_sat_MR[host][i]) > 0:
            mr_bright_sat = np.min(pred_015_sat_MR[host][i])
            pred_015_mag_gap[host].append(mr_host-mr_bright_sat)
        else: 
            pred_015_mag_gap[host].append(-15)

rand_arr_pred_015_mag_gap = []
for i in range(5000):
    tot = 0
    for host in pred_015_mag_gap.keys():
        random = np.random.randint(len(pred_015_mag_gap[host]))
        rand_arr_pred_015_mag_gap.append(pred_015_mag_gap[host][random])

rand_arr_pred_01_mag_gap = []
for i in range(5000):
    tot = 0
    for host in pred_01_mag_gap.keys():
        random = np.random.randint(len(pred_01_mag_gap[host]))
        rand_arr_pred_01_mag_gap.append(pred_01_mag_gap[host][random])

rand_arr_pred_02_mag_gap = []
for i in range(5000):
    tot = 0
    for host in pred_02_mag_gap.keys():
        random = np.random.randint(len(pred_02_mag_gap[host]))
        rand_arr_pred_02_mag_gap.append(pred_02_mag_gap[host][random])

pred_01_mag_gap_no_zeros = {}
for host in pred_01_sat_MR.keys():
    pred_01_mag_gap_no_zeros[host] = []
    if host in completed_hosts['HOSTID']:
        index = df_completed_hosts[df_completed_hosts['HOSTID'] == host].index.values
        mr_host = completed_hosts['K_ABS'][index][0]
    for i in range(len(pred_01_sat_MR[host])):
        if len(pred_01_sat_MR[host][i]) > 0:
            mr_bright_sat = np.min(pred_01_sat_MR[host][i])
            pred_01_mag_gap_no_zeros[host].append(mr_host-mr_bright_sat)

pred_02_mag_gap_no_zeros  = {}
for host in pred_02_sat_MR.keys():
    pred_02_mag_gap_no_zeros[host] = []
    if host in completed_hosts['HOSTID']:
        index = df_completed_hosts[df_completed_hosts['HOSTID'] == host].index.values
        mr_host = completed_hosts['K_ABS'][index][0]
    for i in range(len(pred_02_sat_MR[host])):
        if len(pred_02_sat_MR[host][i]) > 0:
            mr_bright_sat = np.min(pred_02_sat_MR[host][i])
            pred_02_mag_gap_no_zeros[host].append(mr_host-mr_bright_sat)

mean_mag_gap_01_no_zeros= {}
for host in pred_01_mag_gap_no_zeros.keys():
    mean_mag_gap_01_no_zeros[host] = np.mean(pred_01_mag_gap_no_zeros[host])
mean_mag_gap_02_no_zeros= {}
for host in pred_02_mag_gap_no_zeros.keys():
    mean_mag_gap_02_no_zeros[host] = np.mean(pred_02_mag_gap_no_zeros[host])

std_mag_gap_01_no_zeros= {}
for host in pred_01_mag_gap_no_zeros.keys():
    std_mag_gap_01_no_zeros[host] = np.std(pred_01_mag_gap_no_zeros[host])
std_mag_gap_02_no_zeros= {}
for host in pred_02_mag_gap_no_zeros.keys():
    std_mag_gap_02_no_zeros[host] = np.std(pred_02_mag_gap_no_zeros[host])