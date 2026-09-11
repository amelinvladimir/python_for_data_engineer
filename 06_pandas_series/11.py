import pandas as pd

orders = pd.read_csv("./../data/01_retailpulse_csv/marketing_campaigns.csv") 

print("Размер:", orders.shape)

print("\nСтолбцы:")
print(orders.columns)

print("\nТипы:")
print(orders.dtypes)

print("\nПервые строки:")
print(orders.head())

print("\nСтатистика stabudgettus:")
print(orders["budget"].describe())