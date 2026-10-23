# Обработка некорректных дат

import pandas as pd

df = pd.DataFrame({
    "event_time": [
        "2026-10-22 10:00:00",
        "неизвестно",
        "2026-10-23 12:30:00",
    ]
})

df["event_time"] = pd.to_datetime(
    df["event_time"],
    errors="coerce"
)

print(df)