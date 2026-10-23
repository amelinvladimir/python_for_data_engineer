# Пример: Пропуски в количестве продаж

import pandas as pd

df = pd.DataFrame({
    "product": ["A", "B", "C", "D"],
    "quantity": [10, None, 5, None],
})

print(df["quantity"].isna().sum())

df["quantity"] = df["quantity"].fillna(0)

print(df)