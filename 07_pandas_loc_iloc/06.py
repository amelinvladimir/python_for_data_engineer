import pandas as pd

orders = pd.DataFrame({
    "order_id": [1001, 1002, 1003, 1004, 1005],
    "customer_id": [101, 102, 101, 103, 102],
    "amount": [5000, 15000, 8000, 23000, 12000],
    "status": [
        "completed",
        "completed",
        "cancelled",
        "completed",
        "completed"
    ]
})

orders = orders.set_index("order_id")

# Фильтрация через loc
print(orders.loc[orders["amount"] > 10000])

print(orders.loc[
    orders["amount"] > 10000,
    ["customer_id", "amount"]
])

