import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# Open data
path_file = 'selling_data.csv'
df = pd.read_csv(path_file,index_col=0)

# Create Frequency Distribution Table
df.rename(columns={'n_sell_icecream':'Frequency'},inplace=True)

# Create Bar Char
df.plot.bar(rot=0, title='Sales')

# Create Pie Char
df['Relative frequency (%)'] = (df/df.sum())*100
df.plot.pie(y='Relative frequency (%)',autopct='%1.1f%%', title='Sales')

# Create Pareto diagram
df.sort_values(by='Frequency',ascending=False,inplace=True)
df['Cumulative Frequency %'] = (df.iloc[:,0].cumsum()/df.iloc[:,0].sum())*100
ax = df.plot.bar(y='Frequency',rot=0, title='Sales')
ax1 = df.plot(y='Cumulative Frequency %',color='r', style='.-',secondary_y=True,ax=ax)
ax1.set_ylim(0,115)
plt.show()
