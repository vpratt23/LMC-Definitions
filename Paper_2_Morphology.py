"""
Creates a Dictionary of PAPER 2 Hosts that catalogs their morphology to various levels of detail

The most relevant dictionary this creates is df_morph_prop_condensed, which divides the paper 2 hosts into Spirals and Ellipticals

"""
import pandas as pd

bonus_prop_c = {'Name': ['nsa126115', 'nsa129237', 'nsa129387', 'nsa132339', 'nsa133115', 'nsa133355', 'nsa13927', 'nsa139467', 'nsa141465', 'nsa143856', 'nsa144953', 'nsa145729', 'nsa145879', 'nsa147100', 'nsa147606', 'nsa149781', 'nsa149977', 'nsa150887', 'nsa157374', 'nsa161174', 'nsa163956', 'nsa165536', 'nsa165707', 'nsa165980', 'nsa166313', 'nsa32', 'nsa33446', 'nsa3469', 'nsa51348', 'nsa61945', 'nsa69028', 'nsa94340', 'pgc18880', 'pgc66318', 'pgc66934', 'pgc67782', 'pgc67817', 'nsa145372', 'nsa35340', 'nsa133549', 'nsa140458', 'nsa16235', 'pgc64725'], 'K_band': [1.46, 1.089, 1.282, 1.176, 1.025, 1.245, 1.082, 1.204, 1.80, 1.178, 1.10, 1.108, 1.034, 1.08, 1.035, 1.0496, 1.186, 8.351, 1.099, 1.247, 1.047, 1.187, 1.017, 1.161, 1.0684, 1.221, 1.139, 1.122, 1.236, 1.123, 1.0919, 1.099, 1.130, 1.023, 1.0798, 1.168, 1.023, 1.197, 1.156, 'NaN', 'NaN', 'NaN', 'NaN'], 'R_band': [1.14, 'NaN', 'NaN', 1.183, 1.19, 1.251, 1.158, 1.233, 1.172, 1.678, 1.263, 1.183, 'NaN', 'NaN', 1.497, 1.292, 1.266, 1.135, 1.211, 1.256, 1.213, 1.197, 1.281, 1.254, 1.164, 1.12, 1.184, 1.305, 1.245, 1.303, 1.214, 1.279, 1.244, 1.107, 1.11, 1.272, 1.131, 1.232, 1.364, 'NaN', 'NaN', 'NaN', 'NaN'], 'Morphology': ['SAbc', 'S', 'SAB(rs)c', 'SB(r)a', 'E3', 'SA(s)bc', 'SAB(r)a', 'SAB(rs)c', '(R)SB(r)0/a', 'SAB(s)c', 'Sa', 'SB(rs)b', 'S0^0', 'SAB(rs)c', 'S0', 'S0^0', 'Sab', 'SB(rs)bc', '(R)SAB0^+(rs)', 'SA(r)b', 'Sbc', 'SB(r)0/a', 'Sb', 'SBdm', 'SA(r)c', 'SA(s)c', 'SB(s)b', 'SAbc', '(R)SA(rs)b', 'SAB(r)b', '(R)SAB(r)a', '(R)SB(rs)ab', 'SB(rs)bc', 'E6', 'SBa', 'Sbc', 'SA0^-', 'Sc?', 'Sa', 'Sc', 'SAbc', 'Sa', 'E5']}
df_bonus_prop_c = pd.DataFrame(bonus_prop_c)
df_end = df_bonus_prop_c.drop([0, 2, 4, 6, 20, 22, 23])
df_updated = df_end.reset_index()
df_morph_prop={}
index = -1
for key in df_updated['Name']:
    index = index+1
    if df_updated['Morphology'][index] == 'SAbc': 
        df_morph_prop[key] = 'SA'
    if df_updated['Morphology'][index]== 'SA(r)c':
        df_morph_prop[key] = 'SA'
    if df_updated['Morphology'][index] =='SA(s)bc' :
        df_morph_prop[key] = 'SA'
    if df_updated['Morphology'][index]== 'SA(r)b': 
        df_morph_prop[key] = 'SA'
    if df_updated['Morphology'][index]==  'SA(s)c' :
        df_morph_prop[key] = 'SA'
    if df_updated['Morphology'][index] == '(R)SA(rs)b':
        df_morph_prop[key] = 'SA'
    if df_updated['Morphology'][index] == 'SA0^-':
        df_morph_prop[key] = 'SA'
    if 'SAB' in df_updated['Morphology'][index]:
        df_morph_prop[key] = 'SAB'
    if 'SB' in df_updated['Morphology'][index]:
        df_morph_prop[key] = 'SB'
    if 'S0' in df_updated['Morphology'][index]:
        df_morph_prop[key] = 'S0'
    if df_updated['Morphology'][index] == 'S':
        df_morph_prop[key] = 'S'
    if df_updated['Morphology'][index] == 'Sa': 
        df_morph_prop[key] = 'S'
    if df_updated['Morphology'][index] == 'Sab':
        df_morph_prop[key] = 'S'
    if df_updated['Morphology'][index] == 'Sbc': 
        df_morph_prop[key] = 'S'
    if df_updated['Morphology'][index] == 'Sb':
        df_morph_prop[key] = 'S'
    if df_updated['Morphology'][index] == 'Sc?':
        df_morph_prop[key] = 'S'
    if df_updated['Morphology'][index] == 'Sc':
        df_morph_prop[key] = 'S'
    if 'E' in df_updated['Morphology'][index]:
        df_morph_prop[key] = 'E'
df_morph_prop_condensed = {}
index = -1
for key in df_morph_prop.keys():
    index = index+1
    if df_morph_prop[key] == 'S0':
        df_morph_prop_condensed[key] = 'E/S0'
    if df_morph_prop[key] == 'S':
        df_morph_prop_condensed[key] = 'SAB'
    if df_morph_prop[key] == 'SA':
        df_morph_prop_condensed[key] = 'SAB'
    if df_morph_prop[key] == 'SB':
        df_morph_prop_condensed[key] = 'SAB'
    if df_morph_prop[key] == 'SAB':
        df_morph_prop_condensed[key] = 'SAB'
    if df_morph_prop[key] == 'E':
        df_morph_prop_condensed[key] = 'E/S0'
