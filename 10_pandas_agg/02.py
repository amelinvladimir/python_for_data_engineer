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

# Бизнес задаёт вопросы:
# 1. Какая выручка по городам?
# 2. Сколько заказов в каждой категории?
# 3. Какой средний чек?
# 4. Сколько заказов в каждом статусе?

revenue_by_city = orders.groupby("city")["amount"].sum()
print(revenue_by_city)


# еще примеры:

avg_receipt_by_city = orders.groupby("city")["amount"].mean()
print(avg_receipt_by_city)


orders_cnt_by_status = orders.groupby("status").size()
print(orders_cnt_by_status)

# count() считает непустые значения конкретного столбца, а size() — строки группы. Если в столбце есть NaN, результаты могут различаться.

orders_with_payment_cnt_by_status = orders.groupby("status").count()
print(orders_with_payment_cnt_by_status)