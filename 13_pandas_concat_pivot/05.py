# Практические примеры

import pandas as pd

# Собрать выгрузки за два дня

day_1 = pd.DataFrame({
    "order_id": [101, 102],
    "amount": [5000, 3000]
})

day_2 = pd.DataFrame({
    "order_id": [103, 104],
    "amount": [7000, 2000]
})

orders = pd.concat([day_1, day_2], ignore_index=True)

print(orders)