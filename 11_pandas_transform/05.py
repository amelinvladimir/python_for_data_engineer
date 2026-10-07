# Практический кейс: сравнение заказа со средним чеком города

import pandas as pd

orders = pd.DataFrame({
    "order_id": [1001, 1002, 1003, 1004, 1005, 1006],
    "city": ["Москва", "Москва", "Тверь", "Тверь", "Москва", "Тверь"],
    "amount": [10000, 30000, 5000, 15000, 20000, 10000],
    "status": ["completed", "canceled", "completed", "canceled", "completed", "canceled"]
})

orders["city_average"] = (
    orders.groupby("city")["amount"].transform("mean")
)

orders["above_average"] = (
    orders["amount"] > orders["city_average"]
)

print(orders)


# получим заказы выше среднего:
result = orders.loc[
    orders["above_average"],
    ["order_id", "city", "amount", "city_average"]
]

print(result)

# Это уже аналитика на уровне отдельных заказов.