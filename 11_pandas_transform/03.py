# filter: оставляем только подходящие группы

# бизнес хочет анализировать только города, в которых было не менее трёх заказов.

import pandas as pd

orders = pd.DataFrame({
    "order_id": [1001, 1002, 1003, 1004, 1005, 1006],
    "city": ["Москва", "Москва", "Тверь", "Тверь", "Москва", "Тверь"],
    "amount": [10000, 30000, 5000, 15000, 20000, 10000]
})

result = orders.groupby("city").filter(
    lambda group: len(group) >= 3
)

print(result)


# Оставляем все строки тех городов, у которых суммарная выручка не меньше 30 000.

result = orders.groupby("city").filter(
    lambda group: group["amount"].sum() > 30000
)

print(result)

# groupby().filter() отбирает целые группы.