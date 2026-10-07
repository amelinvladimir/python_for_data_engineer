# transform() при группировке по нескольким столбцам

import pandas as pd

orders = pd.DataFrame({
    "order_id": [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    "city": [
        "Москва", "Москва", "Москва",
        "Тверь", "Тверь", "Казань", "Казань"
    ],
    "category": [
        "Ноутбуки", "Ноутбуки", "Мониторы",
        "Ноутбуки", "Ноутбуки", "Мониторы", "Мониторы"
    ],
    "amount": [50000, 70000, 25000, 30000, 20000, 40000, 60000]
})

# Наша задача — для каждого заказа рассчитать:
# 1. Выручку по сочетанию города и категории.
# 2. Долю конкретного заказа в этой выручке.

orders["city_category_revenue"] = (
    orders.groupby(["city", "category"])["amount"]
    .transform("sum")
)

orders["order_share"] = (
    orders["amount"] / orders["city_category_revenue"] * 100
)

print(orders)