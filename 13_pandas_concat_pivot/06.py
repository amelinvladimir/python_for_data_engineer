# Практические примеры

import pandas as pd

# Построить сводную таблицу продаж

sales = pd.DataFrame({
    "city": ["Москва", "Москва", "Москва", "Тверь", "Тверь"],
    "category": [
        "Ноутбуки", "Аксессуары", "Ноутбуки",
        "Ноутбуки", "Аксессуары"
    ],
    "amount": [50000, 3000, 70000, 30000, 5000]
})

table = sales.pivot_table(
    index="city",
    columns="category",
    values="amount",
    aggfunc="sum",
    fill_value=0
)

print(table)

# Подготовить данные для визуализации

long = table.reset_index().melt(
    id_vars="city",
    var_name="category",
    value_name="revenue"
)

print(long)