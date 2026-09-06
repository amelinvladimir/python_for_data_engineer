# Замер скорости

import time
import numpy as np

n = 5_000_000

numbers = list(range(n))

start = time.perf_counter()

result = [x * 2 for x in numbers]

python_time = time.perf_counter() - start

numbers_np = np.arange(n)

start = time.perf_counter()

result_np = numbers_np * 2

numpy_time = time.perf_counter() - start

print("Python:", python_time)
print("NumPy:", numpy_time)

# На типичных численных операциях NumPy может выполнять вычисления значительно эффективнее 
# обычных Python-циклов, поскольку его массивы и операции оптимизированы именно под численные вычисления.

# Но главное преимущество — мы можем выражать вычисления как операции над массивами.




# Но сейчас у нас есть проблема.

# Реальный orders — это не просто массив чисел.

# Там есть:
# order_id
# customer_id
# status
# order_total
# created_at

# И нам нужно работать сразу со всеми этими колонками.
# Нужно фильтровать строки, выбирать колонки, группировать данные, объединять таблицы.

# Поэтому на следующей неделе мы познакомимся с Pandas.