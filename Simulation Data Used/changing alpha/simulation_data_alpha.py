
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

#Pre-computed catalogs for halos matched to SAGA hosts
with open(r"sat_alpha_139.pickle", "rb") as f:
    sat139 = pickle.load(f, encoding='latin1')
    
with open(r"host_halo_alpha_139.pickle", "rb") as f:
    host_halo139 = pickle.load(f, encoding='latin1')
    
with open(r"rproj_alpha_139.pickle", "rb") as f:
    rproj139 = pickle.load(f, encoding='latin1')
    
with open(r"vproj_alpha_139.pickle", "rb") as f:
    vproj139 = pickle.load(f, encoding='latin1')
    
with open(r"Mr_alpha_139.pickle", "rb") as f:
    Mr139 = pickle.load(f, encoding='latin1')

with open(r'sat_143.pickle', 'rb') as f:
    sat143 = pickle.load(f, encoding='latin1')
    
with open(r'host_halo_143.pickle', 'rb') as f:
    host_halo143 = pickle.load(f, encoding='latin1')
    
with open(r'rproj_143.pickle', 'rb') as f:
    rproj143 = pickle.load(f, encoding='latin1')
    
with open(r'vproj_143.pickle', 'rb') as f:
    vproj143 = pickle.load(f, encoding='latin1')
    
with open(r'Mr_143.pickle', 'rb') as f:
    Mr143 = pickle.load(f, encoding='latin1')

#Pre-computed catalogs for halos matched to SAGA hosts
with open(r"sat_alpha_146.pickle", "rb") as f:
    sat146 = pickle.load(f, encoding='latin1')
    
with open(r"host_halo_alpha_146.pickle", "rb") as f:
    host_halo146 = pickle.load(f, encoding='latin1')
    
with open(r"rproj_alpha_146.pickle", "rb") as f:
    rproj146 = pickle.load(f, encoding='latin1')
    
with open(r"vproj_alpha_146.pickle", "rb") as f:
    vproj146 = pickle.load(f, encoding='latin1')
    
with open(r"Mr_alpha_146.pickle", "rb") as f:
    Mr146 = pickle.load(f, encoding='latin1')

def draw_Mr_simple(Mr_mean,sigma_M):
    L_mean = 10**((-1.*Mr_mean + 4.81)/2.5 + np.log10(2))
    L= np.random.lognormal(np.log(L_mean),(np.log(10)*sigma_M))
    return -1.*(2.5*(np.log10(L)-np.log10(2))-4.81)

def actual_Mr_for_sats(satex, Mrex):
    x = {}
    for host in satex.keys():
        if len(satex[host])>0:
            x[host] = []
            for i in range(len(Mrex[host])):
                x[host].append(draw_Mr_simple(Mrex[host][i], sigma_M_sats))
    return x  

pred_Mr139 = actual_Mr_for_sats(sat139, Mr139)
pred_Mr143 = actual_Mr_for_sats(sat143, Mr143)
pred_Mr146 = actual_Mr_for_sats(sat146, Mr146)

def predicting_LMCs(satex, Mrex):
    x = {}
    for key in satex.keys():
        x[key] = []
        for i in range(len(satex[key])):
            x[key].append(len(Mrex[key][i][Mrex[key][i]<-18.3]))
    return x
pred_LMC_139 = predicting_LMCs(sat139, pred_Mr139)
pred_LMC_143 = predicting_LMCs(sat143, pred_Mr143)
pred_LMC_146 = predicting_LMCs(sat146, pred_Mr146)

def chance_of_LMCs(predLMC):
    x = {}
    for key in predLMC.keys():
        tot = 0
        for i in range(len(predLMC[key])):
            if predLMC[key][i]>0:
                tot = tot +1
        x[key] = tot/len(predLMC[key])
    return x
chance_LMC_139 = chance_of_LMCs(pred_LMC_139)
chance_LMC_143 = chance_of_LMCs(pred_LMC_143)
chance_LMC_146 = chance_of_LMCs(pred_LMC_146)

def dict_to_array_conversion(dictex):
    x = []
    for key in dictex.keys():
        x.append(dictex[key])
    return x
chance_LMC_139_arr = dict_to_array_conversion(chance_LMC_139)
chance_LMC_143_arr = dict_to_array_conversion(chance_LMC_143)
chance_LMC_146_arr = dict_to_array_conversion(chance_LMC_146)