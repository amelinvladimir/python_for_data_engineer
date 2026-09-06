# Индексация и slicing

import numpy as np

orders = np.array([
    12500,
    3400,
    27800,
    9100,
    45200
])

# Первый:
print(orders[0])

# Последний:
print(orders[-1])

# Третий:
print(orders[2])

# Срез:
print(orders[1:4])

# NumPy использует стандартный Python-синтаксис индексации 
# и расширяет его на многомерные массивы