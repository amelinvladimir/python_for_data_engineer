import pandas as pd

orders = pd.DataFrame({
    "id": [1001, 1002, 1003],
    "price": ["1200", "3500", "0.05"],
    "qty": [2, 1, 5],
    "status": ["C", "C", "R"]
})

orders["price"] = orders["price"].astype(int) # неуспешное преобразование