# Сравнение групп
# В аналитике часто нужно сравнить не отдельные признаки, а группы объектов

# отличается ли средняя выручка между категориями товаров

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

order_items = pd.read_csv("order_items_raw.csv")
orders = pd.read_csv("orders_clean.csv")

order_items = order_items.merge(
    orders,
    on = "order_id",
    how = "left"
)

sns.boxplot(
    data=order_items,
    x="delivery_city",
    y="discount_pct"
)

plt.xticks(rotation=45)
plt.title("Распределение выручки по каналам продаж")
plt.show()