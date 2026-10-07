# Бизнес-метрики: определения
# На примере интернет-магазина:

# Метрика	Формула
# Выручка	sum(amount)
# Количество заказов	count(order_id)
# Средний чек	revenue / orders_count
# Доля города в общей выручке	city_revenue / total_revenue * 100
# Доля заказа в выручке города	amount / city_revenue * 100

import pandas as pd

orders = pd.DataFrame({
    "order_id": [1001, 1002, 1003, 1004, 1005, 1006],
    "city": ["Москва", "Москва", "Тверь", "Тверь", "Москва", "Тверь"],
    "amount": [10000, 30000, 5000, 15000, 20000, 10000],
    "status": ["completed", "canceled", "completed", "canceled", "completed", "canceled"],
    "category": ["Ноутбуки", "Аксессуары", "Мониторы", "Ноутбуки", "Аксессуары", "Мониторы"],
    "customer_id": [1, 2, 1, 3, 4, 5]
})

total_revenue = orders["amount"].sum()
orders_count = orders["order_id"].nunique()
customers_count = orders["customer_id"].nunique()

metrics = pd.Series({
    "revenue": total_revenue,
    "orders_count": orders_count,
    "unique_customers": customers_count,
    "average_order_value": total_revenue / orders_count,
    "revenue_per_customer": total_revenue / customers_count,
    "purchase_frequency": orders_count / customers_count
})

print(metrics)

category_metrics = orders.groupby("category").agg(
    revenue=("amount", "sum"),
    orders_count=("order_id", "nunique")
)

category_metrics["revenue_share"] = (
    category_metrics["revenue"] / total_revenue * 100
)

print(category_metrics)