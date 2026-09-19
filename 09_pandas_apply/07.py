# скорость

import pandas as pd
import numpy as np
import time

n = 1_000_000

df = pd.DataFrame({
    "price": np.random.randint(100, 10000, n),
    "quantity": np.random.randint(1, 10, n)
})

start = time.perf_counter()

df["revenue_apply"] = df.apply(
    lambda row: row["price"] * row["quantity"],
    axis=1
)

apply_time = time.perf_counter() - start



start = time.perf_counter()

df["revenue_vectorized"] = (
    df["price"] * df["quantity"]
)

vectorized_time = time.perf_counter() - start

print(apply_time)
print(vectorized_time)


# apply
# → много вызовов Python-функции

# vectorization
# → операции над массивами