import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


path_file = 'dataset1.csv'
df = pd.read_csv(path_file,sep=';',decimal=',',header=[0,1])

#Task 2
df['Product','Price']=df['Product','Price'].apply(lambda x: float(x.replace('R$','').replace('.','').replace(',','.')))
df['Product','Price'].plot.hist(bins=df['Product','Price'].shape[0])
plt.show()

# Task 3
task_range = np.arange(df['Product','Price'].min(),df['Product','Price'].max()+100000,100000)
df['Product','Price'].plot.hist(bins=task_range)
plt.xticks(task_range)
plt.grid()
plt.show()

# Task 5
plt.plot(df['Product','Area (ft.)'],df['Product','Price'],'.',ms=10)
plt.xlabel('Area (ft.)')
plt.ylabel('Price ($)')
plt.title('Area X Price')
plt.show()

# Task 6
table_freq = pd.DataFrame(df['Customer']['Country'].value_counts())
table_freq.columns=['Frequency']
table_freq['Relative frequency'] = table_freq['Frequency']/table_freq['Frequency'].sum()
table_freq['Cumulative frequecy'] = table_freq['Relative frequency'].cumsum()
print(table_freq)
ax = table_freq.plot.bar(y='Frequency',rot=0)
ax1 = table_freq.plot(y='Cumulative frequecy', color='r', style='.-',secondary_y=True,ax=ax)
ax1.set_ylim(0,1.1)
plt.show()

# Task 7
print('Statistics')
print('Mean     -->',df['Product','Price'].mean())
print('Median   -->',df['Product','Price'].median())
print('Mode     -->',df['Product','Price'].mode().values[0])
print('Skew     -->',df['Product','Price'].skew())
print('Variance -->',df['Product','Price'].var())
print('STD      -->',df['Product','Price'].std())

# Task 8
interpol_table = df.loc[:, (['Product'], ['Price', 'Area (ft.)'])]
print('Covariance  -->',interpol_table.cov().values[0,1])
print('Correlation -->',interpol_table.corr().values[0,1])