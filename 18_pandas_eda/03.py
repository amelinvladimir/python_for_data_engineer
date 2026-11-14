# Квантили и перцентили
import pandas as pd

df = pd.read_csv("order_items_raw.csv")

print(df["revenue"].quantile(0.25))
print(df["revenue"].quantile(0.50))
print(df["revenue"].quantile(0.75))
print(df["revenue"].quantile(0.90))

# Квантили полезны, например, для ответа на вопрос: «Какой заказ по сумме входит в самые крупные 10% заказов?»