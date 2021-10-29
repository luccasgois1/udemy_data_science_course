import pandas as pd
import numpy as np

def select_tvalue(n, alfa, path_ttable='ttable.csv'):
    t_table = pd.read_table(path_ttable,sep=';',decimal=',',index_col=0)
    t_table.columns = t_table.columns.astype(float)

    # Locate columns
    alfa2 = alfa/2
    list_columns = (np.abs(t_table.columns-alfa2)).to_list()
    min_value = min(list_columns)
    i_col = list_columns.index(min_value)

    # Locate row
    if n > 120:
        i_row = -1
    else:
        list_index = (np.abs(t_table.index-n)).to_list()
        min_value = min(list_index)
        i_row = list_index.index(min_value)

    return t_table.iloc[i_row,i_col]


path_file = 'dataset.csv'
df = pd.read_csv(path_file, decimal=',',sep=';',index_col=0)
df1 = df.iloc[:,1]-df.iloc[:,0]

# Task 1
mean_df1 = df1.mean()
std_df1 = df1.std()
print('Task 1')
print('Mean -->',mean_df1)
print('STD  -->',std_df1)

# Task 3
print('Task 3')
CI = .95
alfa = 1. - CI
n = df1.shape[0] - 1
t=select_tvalue(n, alfa)
CI_low = mean_df1 - std_df1*t/np.sqrt(n+1)
CI_high = mean_df1 + std_df1*t/np.sqrt(n+1)
print('CI         -->',CI)
print('t[{0},{1}] -->'.format(n,np.around(alfa/2,5)),t)
print('CI Low     -->',CI_low)
print('CI High    -->',CI_high)
