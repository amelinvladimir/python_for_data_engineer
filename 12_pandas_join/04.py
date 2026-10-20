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

# Чтобы проверить, какие ключи не нашли соответствия, можно использовать indicator=True
result = orders.merge(
    customers,
    on="customer_id",
    how="left",
    indicator=True
)

print(result)

# Столбец _merge содержит значения left_only, right_only или both.