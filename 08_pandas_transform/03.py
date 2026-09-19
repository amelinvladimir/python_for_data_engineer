import pandas as pd

orders = pd.DataFrame({
    "id": [1001, 1002, 1003],
    "price": ["1200", "3500", "800"],
    "qty": [2, 1, 5],
    "status": ["C", "C", "R"]
})

orders = orders.rename(columns={
    "id": "order_id",
    "price": "unit_price",
    "qty": "quantity"
})

print(orders.dtypes)

# astype
orders["unit_price"] = orders["unit_price"].astype(float)

# Проверяем:
print(orders.dtypes)

orders["quantity"] = orders["quantity"].astype(float)
print(orders.dtypes)

orders = orders.astype({
    "quantity": int,
    "unit_price": float
})
print(orders)

