import numpy as np

orders = np.array([
    12500,
    3400,
    27800,
    9100,
    45200,
    6700,
    18300,
    5200,
    31400,
    8900
])

# два варианта:
print(orders.sum())
print(np.sum(orders))

print(orders.mean())
print(np.mean(orders))

print(orders.max())
print(np.max(orders))

# В NumPy многие операции можно вызвать как методом массива или как функцией NumPy. 
# В обычной работе вы будете встречать оба варианта.