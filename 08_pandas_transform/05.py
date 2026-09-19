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

orders["unit_price"] = orders["unit_price"].astype(float)

# Создание нового признака

orders["revenue"] = (
    orders["unit_price"] *
    orders["quantity"]
)

print(orders)