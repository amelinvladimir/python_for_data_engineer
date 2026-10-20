import pandas as pd

orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104],
    "customer_id": [1, 2, 1, 4],
    "amount": [5000, 3000, 7000, 2000]
})

customers = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Анна", "Борис", "Вера"],
    "city": ["Москва", "Тверь", "Казань"]
})

# Если названия ключей отличаются
result = orders.merge(
    customers,
    left_on="customer_id",
    right_on="id",
    how="left"
)

print(result)

# Если ключ называется одинаково с обеих сторон, удобнее on="customer_id".