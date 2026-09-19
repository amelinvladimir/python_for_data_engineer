import pandas as pd

orders = pd.DataFrame({
    "id": [1001, 1002, 1003],
    "price": ["1200", "3500", "800"],
    "qty": [2, 1, 5],
    "status": ["C", "C", "R"]
})

print(orders)

# rename
orders = orders.rename(columns={
    "id": "order_id",
    "price": "unit_price",
    "qty": "quantity"
})

print(orders)

# rename() не изменяет значения данных, он изменяет имена


