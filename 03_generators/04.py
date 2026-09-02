# Генератор vs список

# Список
# создать → хранить всё → обработать

# Весь результат создаётся сразу.
numbers = (x * x for x in range(10_000_000))

# Обрабатываем все значения сразу
max = 0
for number in numbers:
    if number > max:
        max = number

print(max)

# Генератор
# получить → обработать → получить следующий → обработать → ...

# Lazy evaluation — вычислять данные только тогда, когда они действительно нужны.

def get_numbers():
    for number in range(1, 10_000_000):
        yield number * number

numbers = get_numbers()

max = 0
for number in numbers:
    if max < number:
        max = number

print(max)