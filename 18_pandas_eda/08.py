# Практический пример
# Допустим, мы получили данные интернет-магазина

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "category": [
        "Electronics", "Clothing", "Electronics",
        "Books", "Clothing", "Books",
        "Electronics", "Clothing"
    ],
    "revenue": [1000, 500, 1500, 200, 700, 300, 12000, 600]
})

# Сначала знакомимся с данными

print(df.shape)
print(df.info())
print(df.describe())

# Затем исследуем выручку

print("Среднее:", df["revenue"].mean())
print("Медиана:", df["revenue"].median())
print("90-й перцентиль:", df["revenue"].quantile(0.9))

# Строим гистограмму

sns.histplot(data=df, x="revenue", bins=5)
plt.show()

# Проверяем потенциальные выбросы

q1 = df["revenue"].quantile(0.25)
q3 = df["revenue"].quantile(0.75)

iqr = q3 - q1

outliers = df[
    (df["revenue"] < q1 - 1.5 * iqr) |
    (df["revenue"] > q3 + 1.5 * iqr)
]

print(outliers)

# В этом примере заказ на 12 000 заметно отличается от остальных. Но мы пока не знаем, ошибка это или реальная покупка.
# Главный вывод: одномерный анализ помогает понять каждый признак по отдельности, но не объясняет взаимосвязи между ними. Для этого понадобится двумерный анализ.