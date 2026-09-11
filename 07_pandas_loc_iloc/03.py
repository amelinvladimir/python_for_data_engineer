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

print(orders)

# loc: обращение по label

# создаём осмысленный индекс
orders = orders.set_index("order_id")
print(orders)


# теперь можем получать строку по order_id
print(orders.loc[1002])


# Отличие
print(orders.iloc[0]) # первую строку по позиции
print(orders.loc[1001]) # строку, у которой label равен 1001
