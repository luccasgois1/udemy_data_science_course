import pandas as pd
import numpy as np
from scipy.stats import norm,t 

path_file = 'dataset.csv'
df = pd.read_csv(path_file, decimal=',', sep='\t')
df.loc[:,'Date'] = pd.to_datetime(df['Date'],format='%d/%m/%Y')

# Task 1 
df2 = df[df['Date'] >= '2015-01-01'].copy()
df2.index = df2['Date']
df2 = df2[df2['Gender']=='Male']
df2 = df2[df2['Country']=='United States']
df2 = df2.loc[:,'Size (US)']
df2 = df2.groupby(pd.Grouper(freq='MS')).value_counts()
idx = pd.date_range('2015-01-01','2016-12-31',freq='MS')
df2 = df2.reindex( pd.MultiIndex.from_product([idx,df2.index.levels[1]]),fill_value=0)

df2_mean = df2.groupby(level=1).mean()
df2_sem = df2.groupby(level=1).sem()
n = idx.shape[0]
ci = .95
alfa = 1- ci
T = t.ppf(ci+alfa/2, n-1)
df2_me = df2_sem*T
df2_ci = pd.DataFrame()
df2_ci['low'] = df2_mean - df2_me
df2_ci['high'] = df2_mean + df2_me
Number_pairs = df2_ci['high'].apply(np.ceil)
print('Table with number of pairs for male in USA stores[Based on 2015 - 2016 data]: ')
print(Number_pairs)

# Task 3
df3 = df[df['Date'] >= '2016-01-01'].copy()
df3.index = df3['Date']
df3 = df3[df3['Gender']=='Female']

# Shop GER1
df_ger1 = df3[df3['Shop']=='GER1']
df_ger1 = df_ger1.loc[:,'Size (US)']
df_ger1 = df_ger1.groupby(pd.Grouper(freq='MS')).value_counts()
idx_ger1 = pd.date_range('2016-01-01','2016-12-31',freq='MS')
df_ger1 = df_ger1.reindex( pd.MultiIndex.from_product([idx_ger1,df_ger1.index.levels[1]]),fill_value=0)
df_ger1_mean = df_ger1.groupby(level=1).mean()
df_ger1_var = df_ger1.groupby(level=1).var()
n_ger1 = idx_ger1.shape[0]

# Shop GER2
df_ger2 = df3[df3['Shop']=='GER2']
df_ger2 = df_ger2.loc[:,'Size (US)']
df_ger2 = df_ger2.groupby(pd.Grouper(freq='MS')).value_counts()
idx_ger2 = pd.date_range('2016-01-01','2016-12-31',freq='MS')
df_ger2 = df_ger2.reindex( pd.MultiIndex.from_product([idx_ger2,df_ger2.index.levels[1]]),fill_value=0)
df_ger2_mean = df_ger2.groupby(level=1).mean()
df_ger2_var = df_ger2.groupby(level=1).var()
n_ger2 = idx_ger2.shape[0]

list_n = [n_ger1, n_ger2]
ci_ger = .90
alfa_ger = 1- ci_ger
T_ger = t.ppf(ci_ger+alfa_ger/2, sum(list_n)-len(list_n))

pooled_var_ger = ((list_n[0]-1)*df_ger1_var+(list_n[1]-1)*df_ger2_var)/(list_n[0]+list_n[1]-len(list_n))
margin_error_ger = T_ger*np.sqrt(pooled_var_ger/list_n[0]+pooled_var_ger/list_n[1])
df_ci_ger = pd.DataFrame()
df_ci_ger['low'] = np.around(df_ger1_mean - df_ger2_mean - margin_error_ger,2)
df_ci_ger['high'] = np.around(df_ger1_mean - df_ger2_mean + margin_error_ger,2)
df_ci_ger['Best_performance'] = 'None of the shops'
df_ci_ger.loc[df_ci_ger['low']>=0,'Best_performance'] = 'GER1'
df_ci_ger.loc[df_ci_ger['high']<=0,'Best_performance'] = 'GER2'
print('Table with comparison of GER1 and GER2 stores[Based on data and 90% Confidence]: ')
print(df_ci_ger)