import pandas as pd

daily_revenue = pd.Series([100, 200, 300, 200, 400])

result = daily_revenue.rolling(
    window=3,
).mean()

print(result)

result = daily_revenue.rolling(
    window=3,
    min_periods=1,
).mean()

print(result)