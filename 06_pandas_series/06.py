# Index и columns

import pandas as pd

orders = pd.DataFrame({
    "order_id": [1001, 1002, 1003],
    "amount": [5000, 15000, 8000],
    "status": ["completed", "completed", "cancelled"]
})

# индекс
print(orders.index)

# Колонки
print(orders.columns)

# Важно:
# index — метки строк;
# columns — имена столбцов.