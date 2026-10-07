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

# бизнес хочет сразу:
# - сумму продаж;
# - средний чек;
# - минимальный заказ;
# - максимальный заказ;
# - количество заказов.

result = orders.groupby("city").agg({
    "amount": ["sum", "mean", "min", "max"],
    "order_id": "count"
})

print(result)