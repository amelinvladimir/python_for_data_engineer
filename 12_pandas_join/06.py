# Практические примеры

import pandas as pd

orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104],
    "customer_id": [1, 2, 1, 4],
    "amount": [5000, 3000, 7000, 2000]
})

customers = pd.DataFrame({
    "customer_id": [1, 2, 3],
    "name": ["Анна", "Борис", "Вера"],
    "city": ["Москва", "Тверь", "Казань"]
})

# Получить все заказы и добавить сведения о клиентах
result = orders.merge(
    customers,
    on="customer_id",
    how="left",
    validate="many_to_one"
)

print(result)

# Найти заказы без клиента в справочнике

result = orders.merge(
    customers,
    on="customer_id",
    how="left",
    indicator=True
)

unmatched = result[result["_merge"] == "left_only"]

print(unmatched[["order_id", "customer_id", "amount"]])

# Сравнить количество строк до и после объединения

print("До объединения:", len(orders))

result = orders.merge(
    customers,
    on="customer_id",
    how="left"
)

print("После объединения:", len(result))