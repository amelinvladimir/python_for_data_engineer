# Series и NumPy

import numpy as np
import pandas as pd

values = np.array([100, 200, 300])
series = pd.Series(values)

print(series)

# Можно получить NumPy-представление
print(series.to_numpy())

# в Pandas появляется дополнительная информация:
# values + index