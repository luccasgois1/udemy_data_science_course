import pandas as pd
from scipy.stats import t

path_file = 'dataset.csv'
df = pd.read_csv(path_file,decimal=',',sep=';',index_col=0)
df.loc['Sample Variances',:]= df.loc['Std. deviation',:]**2

nx = df.loc['Sample size','Monday']
ny = df.loc['Sample size','Saturday']
varx = df.loc['Sample Variances','Monday']
vary = df.loc['Sample Variances','Saturday']
pooled_variance = ((nx-1)*varx+(ny-1)*vary)/(nx+ny-2)

mean_mon = df.loc['Mean','Monday']
mean_sat = df.loc['Mean','Saturday']
T = (mean_mon-mean_sat)/((pooled_variance/nx+pooled_variance/ny)**.5)
p = 1 - t.cdf(T,nx+ny-2)
alfa = 0.05
if p < alfa:
    print(f'The null hipotesis is rejected for alfa={alfa:.2f}')
else:
    print(f'The null hipotesis is acepted for alfa={alfa:.2f}')
