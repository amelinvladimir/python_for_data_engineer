# Одномерный и двумерный массив
import numpy as np

orders = np.array([100,200,300,400])

print(orders.shape)
print(orders.ndim)
print(orders.size)

sales = np.array([
    [100, 200, 300],
    [400, 500, 600]
])

print(sales.shape)
print(sales.ndim)
print(sales.size)

# 2 строки и 3 столбца.

#         День 1  День 2  День 3
# Неделя 1  100     200     300
# Неделя 2  400     500     600