# Расчёт длительности

import pandas as pd

df = pd.DataFrame({
    "order_created": ["2026-10-22 10:00:00", "2026-10-22 11:30:00"],
    "order_delivered": ["2026-10-22 12:00:00", "2026-10-22 15:00:00"],
})

df["order_created"] = pd.to_datetime(df["order_created"])
df["order_delivered"] = pd.to_datetime(df["order_delivered"])

df["delivery_minutes"] = (
    df["order_delivered"] - df["order_created"]
).dt.total_seconds() / 60

print(df)