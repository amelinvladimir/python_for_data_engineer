# Crosstab — анализ сочетаний категорий

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

result = pd.crosstab(
    order_items["payment_method"],
    order_items["delivery_city"],
    values = order_items["revenue"],
    aggfunc= "sum"
)

print(result)

# Можно получить доли внутри каждой группы

result = pd.crosstab(
    order_items["payment_method"],
    order_items["delivery_city"],
    values = order_items["revenue"],
    aggfunc= "sum",
    normalize="index"
)

print(result)

# Это полезно, когда мы сравниваем структуру способов оплаты разных городов