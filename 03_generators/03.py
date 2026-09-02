def numbers():
    print("Начало")
    yield 1

    print("После первого yield")
    yield 2

    print("После второго yield")
    yield 3

generator = numbers()

print(next(generator))
print(next(generator))
print(next(generator))