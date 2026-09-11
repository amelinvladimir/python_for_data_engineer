# Первичное исследование

import pandas as pd

orders = pd.read_csv("./../data/01_retailpulse_csv/marketing_campaigns.csv") 

# Первые строки
print(orders.head())


# Последние строки
print(orders.tail())


# Размер
print(orders.shape)


# Названия столбцов
print(orders.columns)


# Количество столбцов
print(len(orders.columns))


# Индекс
print(orders.index)


# Типы всех колонок
print(orders.dtypes)
print(orders.info())


# Простая аналитика
print(orders["budget"].sum())
print(orders["budget"].mean())
print(orders["budget"].min())
print(orders["budget"].max())


# Количество заказов
print(len(orders))
print(orders.shape[0])


# Показать
orders["budget"].describe()