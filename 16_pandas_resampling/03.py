import pandas as pd

df = pd.DataFrame({
    "store": ["A", "A", "A", "B", "B"],
    "date": pd.to_datetime([
        "2026-10-20", "2026-10-21", "2026-10-22",
        "2026-10-20", "2026-10-21",
    ]),
    "revenue": [100, 200, 300, 400, 100],
})

df = df.sort_values(["store", "date"])
df["total"] = df.groupby("store")["revenue"].cumsum()

print(df)