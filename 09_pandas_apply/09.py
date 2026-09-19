# Практический RetailPulse-кейс

import pandas as pd

orders = pd.DataFrame({
    "price": [1200, 3500, 800, 22000],
    "quantity": [2, 1, 5, 1],
    "cost": [800, 2500, 500, 15000]
})

orders["revenue"] = (
    orders["price"] *
    orders["quantity"]
)

orders["profit"] = (
    orders["revenue"] -
    orders["cost"]
)

orders["margin"] = (
    orders["profit"] /
    orders["revenue"] *
    100
)

print(orders)

# Мы построили маленький pipeline.