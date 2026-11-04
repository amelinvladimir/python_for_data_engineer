import pandas as pd

df = pd.DataFrame({
    "order_id": [1, 2, 3, 3],
    "quantity": [2, -1, 5, -1],
    "price": [100, 200, -50, 300],
})

checks = {
    "duplicate_order_id": df["order_id"].duplicated().sum(),
    "negative_quantity": (df["quantity"] < 0).sum(),
    "negative_price": (df["price"] < 0).sum(),
}

print(checks)