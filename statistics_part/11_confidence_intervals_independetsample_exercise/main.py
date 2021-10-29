# CONFIDENCE INTERVALS
# INDEPENDENT SAMPLES
# KNOWN POPULATION VARIANCES

import pandas as pd
import numpy as np
from scipy.stats import norm


path_file = 'dataset.csv'
df = pd.read_csv(path_file, sep=';',index_col=0)
df['Difference'] = df['Engineering'] - df['Management']
df.loc['Population std','Difference'] = np.sqrt( np.power(df.loc['Population std','Engineering'],2)/df.loc['Size','Engineering'] + np.power(df.loc['Population std','Management'],2)/df.loc['Size','Management'])

CI = 0.99
alfa = 1 - CI
z = norm.ppf(alfa/2)
z = np.abs(z)

CI_low = df.loc['Sample mean','Difference'] - df.loc['Population std','Difference']*z
CI_high = df.loc['Sample mean','Difference'] + df.loc['Population std','Difference']*z

print(df)
print('\nCI -->',CI)
print('Z[{0:.4f}] -->'.format(alfa/2),z)
print('CI low:',CI_low)
print('CI high:',CI_high)