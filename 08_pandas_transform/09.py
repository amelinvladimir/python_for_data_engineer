# map с функцией

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

orders = orders.astype({
    "unit_price": float,
    "quantity": int
})

orders = orders.assign(
    revenue=orders["unit_price"] * orders["quantity"],
    discount=lambda df: df["revenue"] * 0.10,
    net_revenue=lambda df: df["revenue"] - df["discount"]
)

orders["status"] = orders["status"].map(
    lambda x: x.lower()
)

print(orders["status"])

# Если для операции уже существует векторизованный метод Pandas, обычно лучше использовать его.