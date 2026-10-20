# Как контролировать кардинальность 

import pandas as pd

orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104],
    "customer_id": [1, 2, 1, 4],
    "amount": [5000, 3000, 7000, 2000]
})

customers = pd.DataFrame({
    "customer_id": [1, 2, 3],
    "name": ["Анна", "Борис", "Вера"],
    "city": ["Москва", "Тверь", "Казань"]
})

customers_bad = pd.DataFrame({
    "customer_id": [1, 1, 2],    
    "name": ["Анна", "Анна (дубликат)", "Борис"]
})

# В merge() есть параметр validate
result = orders.merge(
    customers,
    on="customer_id",
    how="left",
    validate="many_to_one"
)

print(result)



result = orders.merge(
    customers_bad,
    on="customer_id",
    how="left",
    validate="many_to_one"
)

print(result)

# validate проверяет, что ключ в правой таблице уникален, а в левой может повторяться.

# validate	                Что проверяет
# "one_to_one"	            Ключ уникален с обеих сторон
# "one_to_many"	            Ключ уникален слева
# "many_to_one"	            Ключ уникален справа
# "many_to_many"	        Разрешает повторения с обеих сторон; строгой проверки уникальности не делает