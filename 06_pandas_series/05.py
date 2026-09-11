# DataFrame

import pandas as pd

orders = pd.DataFrame({
    "order_id": [1001, 1002, 1003],
    "amount": [5000, 15000, 8000],
    "status": ["completed", "completed", "cancelled"]
})

print(orders)

#               DataFrame
#                    │
#         ┌──────────┼──────────┐
#         ↓          ↓          ↓
#     order_id     amount     status
#        ↓           ↓          ↓
#      Series      Series     Series

# То есть DataFrame можно представить как набор Series, выровненных по одному индексу.