import numpy as np
import pandas as pd

path_file = 'dataset.csv'
interval = 6

df = pd.read_csv(path_file)
i_value = float(df.min())
f_value = float(df.max())
length = np.around((f_value-i_value)/6) # Para distribuicao de frequencia com intervalos arredondados
# length = (f_value-i_value)/6 # Para distribuicao de frequencia com intervalos precisos
list_interval = np.arange(i_value,f_value+0.9*length,length)
list_freq = []

for index,i in enumerate(list_interval[:-1]):
    if index == 0:
        freq = df.query('{0} <= Dataset <= {1}'.format(i, list_interval[index+1])).shape[0]
    else:
        freq = df.query('{0} < Dataset <= {1}'.format(i, list_interval[index+1])).shape[0]
    list_freq.append(freq)

df1 = pd.DataFrame({'Value_i':list_interval[:-1],'Value_f':list_interval[1:],'Freq':list_freq})
df1['Relative Freq'] = df1['Freq']/df1['Freq'].sum()
print(df1)
