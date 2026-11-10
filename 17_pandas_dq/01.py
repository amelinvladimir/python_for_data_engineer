import pandas as pd

df = pd.DataFrame({
    "amount": [10, 12, 11, 13, 12, 14, 100]
})

q1 = df["amount"].quantile(0.25)
q3 = df["amount"].quantile(0.75)

print(q1)
print(q3)

iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = df.loc[
    (df["amount"] < lower) |
    (df["amount"] > upper)
]

print(outliers)


# q1 = 11,5
# q3 = 13,5
# iqr = q3 - q1 = 2
# l = q1 - 1,5 * iqr = 11,5 - 1,5 * 2 = 8,5
# m = q3 + 1,5 * iqr = 13,5 + 1,5 * 2 = 16,5