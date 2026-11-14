import pandas as pd

df = pd.read_csv("orders_clean.csv")


print('-----------------     head     -----------------')
print(df.head())
print('-----------------     tail     -----------------')
print(df.tail())
print('-----------------     shape    -----------------')
print(df.shape)
print('-----------------     info     -----------------')
print(df.info())
print('-----------------     nunique  -----------------')
print(df.nunique())
print('-----------------     isna     -----------------')
print(df.isna().sum())
print('-----------------     describe -----------------')
print(df.describe())