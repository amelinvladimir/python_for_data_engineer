# Практический пример - Длительность обработки заявок

import pandas as pd

df = pd.DataFrame({
    "ticket_id": [101, 102, 103],
    "created_at": [
        "2026-10-22 09:00:00",
        "2026-10-22 10:15:00",
        "2026-10-22 12:00:00",
    ],
    "closed_at": [
        "2026-10-22 10:30:00",
        "2026-10-22 12:45:00",
        "2026-10-22 12:30:00",
    ],
})

for col in ["created_at", "closed_at"]:
    df[col] = pd.to_datetime(df[col])

df["resolution_minutes"] = (
    df["closed_at"] - df["created_at"]
).dt.total_seconds() / 60

print(df[["ticket_id", "resolution_minutes"]])


# Извлечение даты и часа

df["created_date"] = df["created_at"].dt.date
df["created_hour"] = df["created_at"].dt.hour

print(df)