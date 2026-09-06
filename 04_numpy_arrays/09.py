# Boolean mask

import numpy as np

orders = np.array([
    12500,
    3400,
    27800,
    9100,
    45200
])

# Какие заказы больше 10 000?

mask = orders > 10_000
print(mask)

large_orders = orders[mask]
print(large_orders)

# Или сразу:
large_orders = orders[orders > 10_000]


# orders > 10_000 создаёт массив логических значений:
# [True, False, True, False, True]

# И этот массив используется как маска.
# Boolean indexing — штатный механизм индексирования ndarray.