import pandas as pd

orders = pd.DataFrame({
    "order_id": [1001, 1002, 1003, 1004, 1005, 1006],
    "city": ["Москва", "Москва", "Тверь", "Тверь", "Москва", "Тверь"],
    "amount": [10000, 30000, 5000, 15000, 20000, 10000]
})

orders["city_average"] = (
    orders.groupby("city")["amount"].transform("mean")
)

print(orders)

# Сумма заказов клиента
orders["city_total"] = (
    orders.groupby("city")["amount"].transform("sum")
)

# Количество заказов в городе
orders["city_orders"] = (
    orders.groupby("city")["order_id"].transform("count")
)

# Доля заказа в выручке города
orders["share"] = (
    orders["amount"] / orders["city_total"] * 100
)

print(orders)