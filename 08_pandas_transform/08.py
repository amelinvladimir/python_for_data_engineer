# map

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

orders = orders.assign(
    revenue=orders["unit_price"] * orders["quantity"],
    discount=lambda df: df["revenue"] * 0.10,
    net_revenue=lambda df: df["revenue"] - df["discount"]
)

status_map = {
    "C": "completed",
    "R": "returned"
}

orders["status"] = orders["status"].map(status_map)

print(orders["status"])