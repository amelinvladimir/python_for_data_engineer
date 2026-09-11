import pandas as pd

orders = pd.DataFrame({
    "order_id": [1001, 1002, 1003, 1004, 1005],
    "customer_id": [101, 102, 101, 103, 102],
    "amount": [5000, 15000, 8000, 23000, 12000],
    "status": [
        "completed",
        "completed",
        "cancelled",
        "completed",
        "completed"
    ]
})

# iloc — integer-location based, то есть обращение по позиции.
# Первая строка.
print(orders.iloc[0])


# Вторая строка.
print(orders.iloc[1])


# Последняя строка.
print(orders.iloc[-1])


# Несколько строк.
print(orders.iloc[0:3])


# Первая строка, третий столбец.
print(orders.iloc[0, 2])


# Первые три строки и первые три столбца.
print(orders.iloc[0:3, 0:3])