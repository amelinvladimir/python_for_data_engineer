# Квантили и перцентили
import pandas as pd

df = pd.read_csv("order_items_raw.csv")

# Или сразу несколько показателей

print(
    df["revenue"].quantile([0.25, 0.5, 0.75, 0.9])
)