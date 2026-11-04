# Resampling — изменение гранулярности по времени

import pandas as pd

df = pd.DataFrame({
    "timestamp": [
        "2026-10-20 09:00",
        "2026-10-20 18:00",
        "2026-10-21 12:00",
        "2026-10-22 15:00",
    ],
    "revenue": [500, 700, 1200, 900],
})

df["timestamp"] = pd.to_datetime(df["timestamp"])

# Индекс DataFrame должен быть временным индексом либо необходимо явно указать временную колонку через параметр on
daily = (
    df.set_index("timestamp")
      .resample("D")["revenue"]
      .sum()
)

print(daily)

# распространённые частоты:
# Частота	Значение
# "h"	    Час
# "D"	    День
# "W"	    Неделя
# "MS"	    Начало месяца
# "ME"	    Конец месяца