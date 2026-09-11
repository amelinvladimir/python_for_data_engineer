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

# Практический пример

# Пусть бизнес спрашивает:
# Покажи ID, клиента и сумму завершённых заказов стоимостью больше 10 000.

result = orders.loc[
    (orders["amount"] > 10000) &
    (orders["status"] == "completed"),
    ["customer_id", "amount"]
]

print(result)

# Или:

result = orders.query(
    "amount > 10000 and status == 'completed'"
)

print(result[["customer_id", "amount"]])