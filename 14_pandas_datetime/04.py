# UTC — единая точка отсчёта для хранения и сопоставления моментов времени между системами.

# Для аналитических систем удобно хранить временные метки событий в UTC, а локальное время использовать при отображении или бизнес-расчётах.

import pandas as pd

df = pd.DataFrame({
    "event_time": [
        "2026-10-22T10:00:00+00:00",
        "2026-10-22T11:00:00+00:00",
    ]
})

df["event_time"] = pd.to_datetime(df["event_time"], utc=True)

print(df)

# Чтобы перевести временные метки в другую зону, используют tz_convert():
df["event_time_stockholm"] = (
    df["event_time"].dt.tz_convert("Europe/Stockholm")
)

print(df)