# Обычная функция

def get_numbers():
    return [1, 2, 3, 4, 5]


numbers = get_numbers()
print(numbers)

# Генераторная функция

def get_numbers_gen():
    for number in range(1, 6):
        yield number

numbers = get_numbers_gen()
print(numbers)

print(next(numbers))
print(next(numbers))
print(next(numbers))

# return:
# вернуть результат и завершить функцию.

# yield:
# выдать значение сейчас, остановить выполнение и продолжить с этого места при следующем запросе.