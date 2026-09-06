import numpy as np

orders = np.array([
    12500,
    3400,
    27800,
    9100,
    45200
])

print(orders)
print(type(orders))

print(orders.shape)  # Какой формы массив?
print(orders.ndim)   # Количество измерений
print(orders.size)   # Количество всех элементов
print(orders.dtype)  # Тип элементов

# NumPy хранит информацию о типе элементов массива, и это важно для вычислений 
# и использования памяти.