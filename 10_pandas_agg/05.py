# Группировка по двум измерениям

import pandas as pd

orders = pd.DataFrame({
    "order_id": [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    "city": [
        "Москва", "Тверь", "Москва", "Казань",
        "Тверь", "Москва", "Казань"
    ],
    "category": [
        "Ноутбуки", "Аксессуары", "Ноутбуки",
        "Мониторы", "Аксессуары", "Мониторы",
        "Ноутбуки"
    ],
    "amount": [50000, 3000, 70000, 25000, 5000, None, 45000],
    "status": [
        "completed", "completed", "cancelled",
        "completed", "completed", "completed", "completed"
    ]
})


# Бизнес-вопрос:
# Сколько продаж приходится на каждую категорию в каждом городе?

result = orders.groupby(
    ["city", "category"]
)["amount"].sum()

print(result)
# появляется MultiIndex — составной индекс из двух уровней.


# Если нужна обычная таблица:
result = result.reset_index()
print(result)


# Можно сразу:
result = orders.groupby(
    ["city", "category"],
    as_index=False
).agg(
    revenue=("amount", "sum"),
    orders_count=("order_id", "count")
)

print(result)