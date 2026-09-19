# Почему apply не всегда хорош

import pandas as pd

orders = pd.DataFrame({
    "price": [1000, 2000, 5000],
    "quantity": [2, 1, 3]
})

def calculate_revenue(row):
    return row["price"] * row["quantity"]

orders["revenue"] = orders.apply(
    calculate_revenue,
    axis=1
)

# Тот же расчёт, но векторизованный

orders["revenue"] = (
    orders["price"] *
    orders["quantity"]
)

print(orders)