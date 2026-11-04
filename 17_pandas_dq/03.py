import pandas as pd

df = pd.DataFrame({
    "price": [100, None, 200, 300],
    "quantity": [1, 2, None, 4],
})

missing_percent = df.isna().mean().mul(100)
print(df.isna().mean())
print(missing_percent)