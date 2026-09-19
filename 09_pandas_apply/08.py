# скорость

import pandas as pd
import numpy as np
import time

n = 1_000_000

df = pd.DataFrame({
    "price": np.random.randint(100, 10000, n),
    "quantity": np.random.randint(1, 10, n)
})

df["revenue_vectorized"] = (
    df["price"] * df["quantity"]
)

print(df.memory_usage(deep=True))
print(df.memory_usage(deep=True).sum())

# Быстродействие — это не только секунды выполнения. Это ещё память, количество копирований данных и объём данных, который мы обрабатываем.