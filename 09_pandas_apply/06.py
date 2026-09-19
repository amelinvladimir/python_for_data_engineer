# Очень важно не превратить урок в “apply 

import pandas as pd
import numpy as np

orders = pd.DataFrame({
    "price": [1000, 2000, 5000],
    "quantity": [2, 1, 3],
    "name": ["TV1", "Tv2", "tv3"]
})

orders["revenue"] = orders["price"] * orders["quantity"]


def calculate_category(row):
    if row["revenue"] >= 50000:
        return "VIP"

    if row["revenue"] >= 10000:
        return "large"

    return "regular"


orders["category"] = orders.apply(
    calculate_category,
    axis=1
)

print(orders)

#  но и тут есть векторизованный вариант

orders["category_v"] = np.select(
    [
        orders["revenue"] >= 50000,
        orders["revenue"] >= 10000
    ],
    [
        "VIP",
        "large"
    ],
    default="regular"
)

print(orders)