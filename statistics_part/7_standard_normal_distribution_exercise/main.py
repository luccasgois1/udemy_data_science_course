import pandas as pd
from matplotlib import pyplot as plt


# Original Dataset
path_file = 'dataset.csv'
df = pd.read_csv(path_file, sep=' ',decimal=',')
df.sort_values(by='Original_dataset',inplace=True)
print(df)

# Normalize
original_mean = df.mean().values[0]
original_std = df.std().values[0]
df['Normalize_dataset'] = (df['Original_dataset']-original_mean)/original_std
print(df)
print('--> Mean')
print(df.mean())
print('--> STD')
print(df.std())

# Figures
plt.figure()
plt.subplot(2,1,1)
df['Original_dataset'].plot.hist()
plt.subplot(2,1,2)
df['Normalize_dataset'].plot.hist()
plt.show()