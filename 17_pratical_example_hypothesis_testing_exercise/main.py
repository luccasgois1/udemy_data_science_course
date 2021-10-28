import pandas as pd
from scipy.stats import t


path_file = 'dataset.csv'
df = pd.read_csv(path_file,decimal=',',sep='\t')
print(df)
d = pd.DataFrame(index=['White','Nonwhite'])
df_white = df[df.loc[:,'Ethnicity'] == 'White'].copy() 
df_nonwhite = df[df.loc[:,'Ethnicity'] != 'White'].copy() 
d['n'] = [df_white.shape[0], df_nonwhite.shape[0]]
d['Mean'] = [df_white.loc[:,'Salary'].mean(), df_nonwhite.loc[:,'Salary'].mean()]
d['Population Variance'] = [df_white.loc[:,'Salary'].var(), df_nonwhite.loc[:,'Salary'].var()]
nx = d.loc['White','n']
ny = d.loc['Nonwhite','n']
varx = d.loc['White','Population Variance']
vary = d.loc['Nonwhite','Population Variance']
pooled_variance = ((nx-1)*varx + (ny-1)*vary)/(nx+ny-2)
T = (d.loc['Nonwhite','Mean']-d.loc['White','Mean'])/((pooled_variance/nx+pooled_variance/ny)**.5)
p = 2*(1 - t.cdf(T,nx+ny-2))
print(d)
print(f'Pooled Variance:{pooled_variance}')
print(f'T-score:{T:.3f}')
print(f'p:{p:.3f}')
alfa = .1
if p < alfa:
    print(f'The null hipotesis is rejected for alfa={alfa:.2f}')
else:
    print(f'The null hipotesis is acepted for alfa={alfa:.2f}')

