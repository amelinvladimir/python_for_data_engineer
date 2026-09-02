# Генераторы как pipeline

# у нас есть заказы 
# orders = ...

# Нам нужны только заказы больше 10 000 рублей.

def read_orders(filename):
    with open(filename) as file:
        next(file)
        print('Step 0')

        for line in file:
            print('Step 1')
            order_id, amount = line.strip().split(",")
            yield {
                "order_id": int(order_id),
                "amount": float(amount)
            }

def filter_orders(orders):
    print('Step 2.0')
    for order in orders:
        print('Step 2')
        if order["amount"] >= 10_000:
            yield order

def add_commission(orders):
    print('Step 3.0')
    for order in orders:
        print('Step 3')
        order["commission"] = order["amount"] * 0.03
        yield order

orders = read_orders("orders.csv")
orders = filter_orders(orders)
orders = add_commission(orders)

for order in orders:
    print(order)

# Источник данных
#       ↓
# filter
#       ↓
# transform
#       ↓
# результат

# Мы можем построить цепочку обработки, при которой данные проходят через несколько этапов, 
# но не обязаны хранить весь промежуточный результат в памяти.