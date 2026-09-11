# Загружаем настоящий dataset

import pandas as pd

orders = pd.read_csv("./../data/01_retailpulse_csv/orders_raw.csv") 

print(orders.head())

# read_csv читает CSV и возвращает DataFrame. 
# 
# Pandas также умеет читать данные порциями через chunksize, 
# что будет особенно полезно позже, когда мы будем говорить о больших данных.