# Пример: Преобразование цены

import pandas as pd

df = pd.DataFrame({
    "product": ["A", "B", "C"],
    "price": ["100", "ошибка", "250"],
})

df["price"] = pd.to_numeric(df["price"], errors="coerce")

print(df)
print("Ошибочных цен:", df["price"].isna().sum())