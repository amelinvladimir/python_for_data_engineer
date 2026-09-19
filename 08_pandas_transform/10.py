# Итог

import pandas as pd

orders = pd.DataFrame({
    "id": [1001, 1002, 1003, 1004],
    "price": ["1200", "3500", "800", "22000"],
    "qty": [2, 1, 5, 1],
    "status": ["C", "C", "R", "C"]
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
    revenue=lambda df: df["unit_price"] * df["quantity"],
    discount=lambda df: df["unit_price"] * df["quantity"] * 0.1
)

orders["status"] = orders["status"].map({
    "C": "completed",
    "R": "returned"
})

print(orders)

# Мы не просто «меняем таблицу». 
# Мы строим из сырых данных аналитические признаки, 
# которые потом будем использовать для фильтрации, 
# группировки, визуализации и построения витрин.