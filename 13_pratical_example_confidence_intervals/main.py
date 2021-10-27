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
