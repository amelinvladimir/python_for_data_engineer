# Scatterplot — диаграмма рассеяния
# Один из наиболее полезных графиков для исследования взаимосвязей — scatterplot.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    "quantity": [1, 2, 3, 4, 5],
    "revenue": [100, 200, 300, 400, 500],
    "discount": [0, 0, 5, 10, 15]
})

sns.scatterplot(
    data=df,
    x="discount",
    y="revenue"
)

plt.title("Количество товаров и выручка")
plt.xlabel("Количество товаров")
plt.ylabel("Выручка")
plt.show()

sns.regplot(
    data=df,
    x="discount",
    y="revenue",
    scatter_kws={'alpha': 0.4},
    line_kws={'color': 'green'}
)

plt.title("Количество товаров и выручка")
plt.xlabel("Количество товаров")
plt.ylabel("Выручка")
plt.show()