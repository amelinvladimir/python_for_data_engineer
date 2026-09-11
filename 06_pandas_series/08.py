# Типы данных
import pandas as pd

orders = pd.DataFrame({
    "order_id": [1001, 1002, 1003],
    "amount": [5000, 15000, 8000],
    "status": ["completed", "completed", "cancelled"]
})

print(orders.dtypes)

# Для аналитика тип данных критически важен

# Например это разные вещи:
# amount = "15000"
# amount = 15000

# Если дата загрузилась строкой:
# "2026-09-01"
# это ещё не полноценный datetime-тип.