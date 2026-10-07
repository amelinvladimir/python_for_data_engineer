# Бизнес-метрики: выручка и средний чек

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

# типичный расчёт:

completed = orders[orders["status"] == "completed"]


# расчет агрегатных функций без применения group_by
metrics = pd.Series({
    "revenue": completed["amount"].sum(),
    "orders_count": completed["order_id"].count(),
    "average_order": completed["amount"].mean()
})

print(metrics)


# если не хотим считать заказы, к которых в amount - NaN:

completed = orders[
    (orders["status"] == "completed") &
    (orders["amount"].notna())
]

metrics = pd.Series({
    "revenue": completed["amount"].sum(),
    "orders_count": completed["order_id"].count(),
    "average_order": completed["amount"].mean()
})

print(metrics)

# А где тогда использовать именованную агрегацию через agg()?
# Она особенно удобна при использовании groupby()