import pandas as pd
import numpy as np


def calc_statistic(y):
    x = y['dataset']
    return [np.around(x.mean()),np.around(x.std()),np.around(x.sem())]


def select_tvalue(n, alfa, path_ttable='ttable.csv'):
    t_table = pd.read_table(path_ttable,sep=';',decimal=',',index_col=0)
    t_table.columns = t_table.columns.astype(float)

    # Locate columns
    alfa2 = alfa/2
    list_columns = (t_table.columns-(alfa/2)).to_list()
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
df = pd.read_csv(path_file)

# Task 1
print('Task 1')
statistics_list = calc_statistic(df)
print('Mean -->{s[0]}\nSt.deviation -->{s[1]}\nStandart error --> {s[2]}\ncomplete!'.format(s=statistics_list))


# Task 3
print('\nTask 3')
CI = 0.99

alfa = np.around(1.0 - CI,5)
n = df.shape[0]-1
t = select_tvalue(n, alfa)
print('t[{0},{1}] = {2}'.format(alfa/2,n, t))

# Task 4
print('\nTask 4')
CI_low = statistics_list[0]-(t*statistics_list[2])
CI_high = statistics_list[0]+(t*statistics_list[2])
print('CI_low: {0}\nCI_high: {1}'.format(CI_low, CI_high))