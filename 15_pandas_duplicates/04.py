# Проверка качества до и после очистки
# Полезно не только очистить данные, но и измерить результат

import pandas as pd

df = pd.DataFrame({
    "product": ["A", "B", "C", "C"],
    "quantity": [10, None, 5, 5],
})

print("Пропуски:", df.isna().sum().to_dict())

print("Строк до очистки:", len(df))
df = df.dropna()
print("Строк после очистки:", len(df))

print("Полные дубликаты: ", df.duplicated().sum())
df = df.drop_duplicates()
print("Строк после удаления дубликатов: ", len(df))