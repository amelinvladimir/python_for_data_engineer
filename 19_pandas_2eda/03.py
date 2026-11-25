# Heatmap — тепловая карта корреляций

# Когда числовых признаков много, удобно построить корреляционную матрицу и отобразить её в виде тепловой карты

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    "quantity": [1, 2, 3, 4, 5],
    "revenue": [100, 200, 300, 400, 500],
    "discount": [0, 0, 5, 10, 15]
})

correlation = df[
    ["quantity", "revenue", "discount"]
].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

plt.title("Корреляционная матрица")
plt.show()

# Тепловая карта помогает быстро обнаружить пары признаков с сильной линейной взаимосвязью.