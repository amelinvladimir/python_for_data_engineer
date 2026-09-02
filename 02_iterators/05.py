# Создаём собственный итератор

class CountIterator:

    def __init__(self, max_value):
        self.current = 0
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.max_value:
            raise StopIteration

        self.current += 1
        return self.current

numbers = CountIterator(5)

for number in numbers:
    print(number)