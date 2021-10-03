import pandas as pd
import numpy as np


def get_z(x):
    
    if x> 0.999:
        return 3.09
    elif x<0.5:
        return 0.0

    x = np.around(x,4)
    path_zfile = 'z_table.csv'
    df_z = pd.read_csv(path_zfile,decimal=',',sep='\t',index_col=[0])
    df_z.columns = list(map(lambda x: float(x.replace(',','.')),df_z.columns))
    loc_values = df_z[df_z.isin([x])].stack()

    # Test if X in Table
    passo = 0.0001
    x_sup = x
    x_inf = x
    while loc_values.shape[0] == 0:
        x_sup += 0.0001
        x_sup = np.around(x_sup,4)
        loc_values = df_z[df_z.isin([x_sup])].stack()
        if loc_values.shape[0] == 0:
            x_inf -= 0.0001
            x_inf = np.around(x_inf,4)
            loc_values = df_z[df_z.isin([x_inf])].stack()
        else:
            break

    choose_value = np.sum(loc_values.index.to_list())/loc_values.index.shape[0]
    choose_value = np.around(choose_value,2)
    
    return choose_value

# Task 1
print('Task 1')
path_file = 'dataset.csv'
df = pd.read_csv(path_file)
sample_mean = np.around(df.mean().values[0],2)
pop_std = 15000
standard_error = np.around(pop_std/np.sqrt(df.shape[0]),2)
print('Sample Mean    -->',sample_mean)
print('Population STD -->',pop_std)
print('Standard Error -->',standard_error)

# Task 2
print('\nTask 2')
CI = 0.9
a = 1 - CI
n = 1 - a/2
z = get_z(n)
print('Z -->',z)

# Task 3
print('\nTask 3')
lim_inf = np.around(sample_mean-standard_error*z,2)
lim_sup = np.around(sample_mean+standard_error*z,2)
print('Intervalo de confiança: {0} a {1}'.format(lim_inf, lim_sup))