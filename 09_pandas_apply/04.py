# Почему apply не всегда хорош

import pandas as pd

orders = pd.DataFrame({
    "price": [1000, 2000, 5000],
    "quantity": [2, 1, 3]
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

orders["is_large"] = orders["revenue"] > 10_000

print(orders)

# Получаем целый набор признаков без Python-циклов.