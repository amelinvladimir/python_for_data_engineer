# concat() — объединение таблиц по строкам и столбцам
# В отличие от merge(), который сопоставляет записи по ключам, concat() соединяет объекты Pandas по выбранной оси.
# Допустим, заказы выгружаются из двух систем или за два разных периода.

import pandas as pd

orders_january = pd.DataFrame({
    "order_id": [101, 102],
    "amount": [5000, 3000]
})

orders_february = pd.DataFrame({
    "order_id": [103, 104],
    "amount": [7000, 2000]
})

# Вертикальное объединение — добавляем строки:

all_orders = pd.concat(
    [orders_january, orders_february],
    ignore_index=True
)

print(all_orders)

# Горизонтальное объединение — добавляем столбцы:

left = pd.DataFrame({
    "order_id": [101, 102],
    "amount": [5000, 3000]
})

right = pd.DataFrame({
    "city": ["Москва", "Тверь"],
    "manager": ["Анна", "Борис"]
})

result = pd.concat([left, right], axis=1)

print(result)

# Здесь столбцы соединяются по индексам, а не по order_id. Если индексы не соответствуют друг другу, данные могут оказаться сопоставлены неверно.

# Правило: если нужно соединить записи по бизнес-ключу, используй merge(). Если нужно добавить строки однотипных таблиц, обычно подходит concat().