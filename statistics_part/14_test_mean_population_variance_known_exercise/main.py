import pandas as pd
import numpy as np
from scipy.stats import norm

path_file = 'dataset.csv'
df = pd.read_csv(path_file)
Ho = 113000
std_pop = 15000
df_mean = df.mean().values[0]
standard_error = std_pop/np.sqrt(df.shape[0])
Z = np.abs((df_mean - Ho)/ standard_error)
alfa = .1
z = np.abs(norm.ppf(alfa/2))

if Z > z:
    print(f'The null hipoteses is rejected: {Z:.2f}>{z:.2f}')
else:
    print(f'The null hipoteses is acepted: {Z:.2f}<={z:.2f}')