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

# Иногда такой код становится плохо читаемым.
print(orders[
    (orders["amount"] > 10000) &
    (orders["status"] == "completed")
])


# Можно использовать query
print(orders.query(
    "amount > 10000 and status == 'completed'"
))

# Примеры query
print(orders.query("amount > 10000"))
print(orders.query("status == 'completed'"))
print(orders.query("status != 'completed'"))
print(orders.query("amount >= 5000 and amount <= 15000"))