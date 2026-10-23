# Некорректные типы

import pandas as pd

df = pd.DataFrame({
    "price": ["100", "250", "unknown", "300"]
})

df["price"] = pd.to_numeric(df["price"], errors="coerce")
print(df)


df = pd.DataFrame({
    "created_at": ["2026-10-22 10:00:00", "2026-10-22 15:00:00", "unknown", "2026-10-22 20:00:00"]
})

df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
print(df)


df = pd.DataFrame({
    "quantity": ["1", "5", "ZaZ", "10"]
})
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").astype("Int64")
print(df)

# Обычный тип int64 не может непосредственно хранить NaN, тогда как pandas Int64 поддерживает пропущенные значения.