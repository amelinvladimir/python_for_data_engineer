# Broadcasting

import numpy as np

unit_price = np.array([
    1200,
    3500,
    800,
    1500,
    22000
])

discount = 0.9
discounted_price = unit_price * discount
print(discounted_price)

# У нас один коэффициент 0.9 и целый массив цен.
# NumPy автоматически применил этот коэффициент к каждому элементу.


# Если у каждого товара своя скидка:
discount = np.array([
    0.9,
    0.8,
    1.0,
    0.95,
    0.85
])

discounted_price = unit_price * discount
print(discounted_price)

# Broadcasting позволяет NumPy выполнять операции 
# над массивами совместимых форм, автоматически сопоставляя их размерности.

# Важно понять сам принцип:
# NumPy может распространить небольшую структуру данных на большую, 
# если их формы совместимы.