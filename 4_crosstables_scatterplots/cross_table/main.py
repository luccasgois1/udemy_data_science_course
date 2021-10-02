from numpy import row_stack
import pandas as pd
from matplotlib import pyplot as plt


path_file = 'dataset.csv'
df = pd.read_csv(path_file,index_col=[0])
df['Unemployed'] = 100-df['Employed']
print(df)
df.plot.bar(rot=0,title='Employment by age group')
plt.show()