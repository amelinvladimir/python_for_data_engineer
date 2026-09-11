import pandas as pd


# DataFrame из нашего магазина
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


# Обычный выбор столбца
print(orders["amount"])

# Несколько
print(orders[["order_id", "amount"]])


# Почему нужны loc и iloc?

# Проблема:
# orders[...]
# хорошо работает для простых случаев.

# Но нам нужно:

# взять конкретные строки;
# взять конкретные столбцы;
# обратиться по имени индекса;
# обратиться по позиции;
# использовать условие.