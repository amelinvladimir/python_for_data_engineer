# аналитический кейс

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

# Сколько заказов?
print(orders.size)

# Какая выручка?
print(orders.sum())

# Средний чек?
print(orders.mean())

# Самый большой заказ?
print(orders.max())

# Сколько заказов дороже 10 000?
print((orders > 10_000).sum())

# Какова выручка только крупных заказов?
large_orders = orders[orders > 10_000]
print(large_orders.sum())

# Какой средний чек среди крупных заказов?
print(large_orders.mean())