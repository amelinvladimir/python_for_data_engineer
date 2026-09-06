import numpy as np

# Есть цена продажи:

prices = np.array([
    1000,
    2000,
    3000,
    4000
])

# И себестоимость:

costs = np.array([
    600,
    1200,
    1800,
    2500
])

# Считаем прибыль:

profit = prices - costs
print(profit)

# Считаем процент прибыли:

profit_percent = profit / prices * 100
print(profit_percent)

# NumPy выполняет операции поэлементно:

# 1000 - 600 = 400
# 2000 - 1200 = 800
# 3000 - 1800 = 1200
# 4000 - 2500 = 1500