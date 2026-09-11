# Получение одного столбца

import pandas as pd

orders = pd.DataFrame({
    "order_id": [1001, 1002, 1003],
    "amount": [5000, 15000, 8000],
    "status": ["completed", "completed", "cancelled"]
})

# Получаем Series
print(orders["amount"])

# Получаем DataFrame
print(orders[["amount"]])