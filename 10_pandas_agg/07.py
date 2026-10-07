# Практический кейс

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

# выручка по городу и категории

completed = orders.query("status == 'completed'")

report = completed.groupby(
    ["city", "category"],
    as_index=False
).agg(
    revenue=("amount", "sum"),
    orders_count=("order_id", "count"),
    average_order=("amount", "mean")
)

print(report)

# groupby отвечает на вопрос «по каким группам считаем», а agg — «какие показатели считаем для каждой группы».