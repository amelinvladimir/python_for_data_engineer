# Анализ категориальных признаков

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("orders_clean.csv")

# Посмотрим, какие есть каналы рекламы
print(df["channel"].value_counts())

# Посмотрим доли каналов рекламы
print(
    df["channel"].value_counts(normalize=True) * 100
)

# Построим график
sns.countplot(
    data=df,
    x="channel",
    order=df["channel"].value_counts().index
)

plt.xticks(rotation=45)
plt.title("Количество заказов по каналам рекламы")
plt.show()

# Такой анализ помогает ответить на вопросы:
# - Какие каналы рекламы встречаются чаще?
# - Есть ли редкие каналы рекламы?
# - Не доминирует ли один канал рекламы?
# - Есть ли канал рекламы с подозрительно малым количеством заказов?