import pandas as pd
from matplotlib import pyplot as plt

path_file = 'dataset.csv'

df = pd.read_csv(path_file,sep='\t')
print(df.skew())

df.hist()
plt.show()