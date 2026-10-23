# Пример: Удаление повторных событий

import pandas as pd

df = pd.DataFrame({
    "event_id": [1, 2, 2, 3],
    "event": ["open", "click", "click", "purchase"],
})

df = df.drop_duplicates(subset=["event_id"], keep="first")

print(df)