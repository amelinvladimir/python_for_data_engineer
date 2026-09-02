# Что происходит внутри for
numbers = [10, 20, 30]

for number in numbers:
    print(number)


# Приблизительно это
iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break

# Важно
# for не получает весь список целиком на каждой итерации. Он работает с итератором и последовательно получает следующий элемент.
