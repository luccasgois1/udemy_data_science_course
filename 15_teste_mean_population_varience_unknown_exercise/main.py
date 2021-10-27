import pandas as pd
import numpy as np
from scipy.stats import t


def test_null_hipotesis(T,tt):
    if T > tt:
        print(f'The null hipotesis is rejected: {T:.2f}>{tt:.2f}')
    else:
        print(f'The null hipotesis is acepted: {T:.2f}<={tt:.2f}')


path_file = 'dataset.csv'
df = pd.read_csv(path_file)
H0 = .4
df_mean = df.mean().values[0]
df_std = df.std().values[0]
df_stand_error = df_std/(df.shape[0]**.5)
T = np.abs((df_mean - H0)/df_stand_error)

#Task 1.1, 1.2 and 1.3
alfa_list = [.05,.01]
p = 2*(1-t.cdf(T, df.shape[0]-1))
for a in alfa_list:
    tt = np.abs(t.ppf(a/2,df.shape[0]-1))
    test_null_hipotesis(T,tt)
    if p < a:
        print(f'The null hipotesis is rejected for alfa={a:.2f}')
    else:
        print(f'The null hipotesis is acepted for alfa={a:.2f}')
    print()
