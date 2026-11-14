import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("order_items_raw.csv")

# Boxplot
# Диаграмма размаха позволяет быстро оценить медиану, квартили и потенциальные выбросы.

sns.boxplot(data=df, x="revenue")

plt.title("Распределение выручки")
plt.show()

# Boxplot особенно полезен при сравнении распределений между группами. Например, при сравнении сумм заказов в разных категориях товаров.