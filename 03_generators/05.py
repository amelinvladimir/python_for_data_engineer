# Нужно ли Python вычислять все 10 миллионов квадратов, если мы остановились на первом подходящем?

def get_numbers():
    for number in range(1, 10_000_000):
        yield number * number

numbers = get_numbers()

for number in numbers:
    if number > 1_000_000:
        print(number)
        break


# Список:
# все данные
# ████████████████████
#         ↓
#   обработка


# Генератор:
# данные → обработка → данные → обработка → ...
#    ↓
# только когда нужны