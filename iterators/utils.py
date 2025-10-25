"""Модуль создания итераторов и генераторов"""


class IterFib:
    """Итератор последовательности Фибоначчи"""

    def __init__(self, num):
        self.max = num
        self.count = -1                     # Счётчик будет инкрементироваться в начале __next__                                 
        self.fib = []

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        match self.count:
            case 0 | 1:
                self.fib.append(self.count)
                return self.fib[self.count]
            case count if 1 < count < self.max:
                self.fib.append(self.fib[count - 2] + self.fib[count - 1])
                return self.fib[self.count]
            case count if count >= self.max:
                raise StopIteration


def gen_fib(num):
    """Генератор последовательности Фибоначчи"""

    count = -1
    fib = []
    while count < num:
        count += 1
        match count:
            case 0 | 1:
                fib.append(count)
                yield fib[count]
            case count if 1 < count < num:
                fib.append(fib[count - 2] + fib[count - 1])
                yield fib[count]


if __name__ == "__main__":

    n = 10
    inst = IterFib(n)
    for i in inst:
        print(i, end=" ")

    n = 15
    print()                             # Для удобочитаемости результатов
    for i in gen_fib(n):
        print(i, end=" ")
    print()
