# Формирование и проверка гипотез
# EDA помогает формировать гипотезы, которые затем можно проверять.

# Например:
# Наблюдение: на графике видно, что заказы с большей скидкой имеют более высокую среднюю сумму.
# Гипотеза: предоставление скидки увеличивает среднюю сумму заказа.

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

# Для начала сравним средние значения

order_items["discount_group"] = (
    order_items["discount_pct"] > 0
).map({
    True: "Скидка",
    False: "Без скидки"
})

result = (
    order_items.groupby("discount_group")["revenue"]
    .agg(["count", "mean", "median"])
)

print(result)

sns.boxplot(
    data=order_items,
    x="discount_group",
    y="revenue"
)
