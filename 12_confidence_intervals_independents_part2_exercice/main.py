# CONFIDENCE INTERVALS
# INDEPENDENT SAMPLES
# UNKNOWN POPULATION VARIANCES BUT ASSUMED TO BE EQUAL
# POOLED VARIANCE FORMULA - S²P = ((NX-1)SX² + (NY -1)SY²) / (NX + NY - 2)

import pandas as pd
import numpy as np
from scipy.stats import t


def statistics_table(x):
    y = pd.DataFrame()
    y['Mean'] = x.mean()
    y['STD'] = x.std()
    y['Size'] = x.count()
    
    return y


def pooled_var(stats_table):

    nn = stats_table.shape[0]
    total_up = 0
    total_down = 0
    for i in range(nn):
        n = stats_table.loc[stats_table.index[i], 'Size']
        s2 = np.power(stats_table.loc[stats_table.index[i],'STD'],2)
        total_up += (n-1)*s2
        total_down += n
    total_down -= nn
    
    return total_up/total_down


path_file = 'dataset.csv'
df = pd.read_csv(path_file, decimal=',', sep=';')
df_stats = statistics_table(df)
p_var = pooled_var(df_stats)
ci = .9
alfa = 1 - ci
t_n_alfa2 = t.ppf(ci+alfa/2,df_stats['Size'].sum()-df_stats['Size'].shape[0])
ci_low = (df_stats['Mean'][0] - df_stats['Mean'][1]) - t_n_alfa2*np.sqrt(p_var/df_stats['Size'][0]+p_var/df_stats['Size'][1])
ci_high = (df_stats['Mean'][0] - df_stats['Mean'][1]) + t_n_alfa2*np.sqrt(p_var/df_stats['Size'][0]+p_var/df_stats['Size'][1])

print('Dataset:\n',df)
print('Pooled Variation:',p_var)
print('Confidence Inverval:',ci)
print('t[{0},{1}]:'.format(df_stats['Size'].sum()-df_stats['Size'].shape[0],alfa/2),t_n_alfa2)
print('CI low:',ci_low)
print('CI high:',ci_high)