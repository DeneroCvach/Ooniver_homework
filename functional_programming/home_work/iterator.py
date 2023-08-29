# Создайте итератор как класс, который возвращает значения от указанных аргументов от “a” до “b”,
# при инициализации класс принимает эти аргументы. протестируйте итератор с помощью “for”


class Iterator:
    def __init__(self, a, b):
        self.start = a
        self.end = b

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        else:
            value = self.start
            self.start += 2
            return value


iterator = Iterator(1, 11)
for num in iterator:
    print(num)
