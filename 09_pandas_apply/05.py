# map vs векторизация

import pandas as pd

orders = pd.DataFrame({
    "price": [1000, 2000, 5000],
    "quantity": [2, 1, 3],
    "name": ["TV1", "Tv2", "tv3"]
})

orders["price"] = orders["price"].map(lambda x: x * 1.2)

# Но лучше:
orders["price"] = orders["price"] * 1.2



orders["name"] = orders["name"].map(lambda x: x.lower())

# Но лучше:
orders["name"] = orders["name"].str.lower()



orders["price"] = orders["price"].map(lambda x: abs(x))

# Но лучше:
orders["price"] = orders["price"].abs()
print(orders)

# Если Pandas уже умеет выполнить операцию над целым Series, 
# не надо заставлять Python вызывать функцию миллион раз.

# Python-функции через apply/map несут дополнительный overhead