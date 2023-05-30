from collections.abc import Iterable


class SquareIterator:
    """
    Класс Итератор Квадрата

    Args:
        number (int): вводное число
    """

    def __init__(self, number: int) -> None:
        self.number = number
        self.count = 0

    def __iter__(self) -> self:
        return self

    def __next__(self) -> int:
        self.count += 1
        if self.count <= self.number:
            return self.count ** 2
        else:
            raise StopIteration


def square_gen(number: int) -> Iterable[int]:
    """
    Функция-генератор для возведения ряда чисел в квадрат

    :param number: входное число от пользователя

    :return: number ** 2
    """
    for i_number in range(1, number + 1):
        yield i_number ** 2


user_number = int(input('Введите число: '))
print('\nРезультат итератора')
sqr = SquareIterator(user_number)
for res in sqr:
    print(res, end=' ')

print('\n\nРезультат функции-генератора')
for res_2 in square_gen(user_number):
    print(res_2, end=' ')

print('\n\nРезультат генераторного выражения')
square_gen_2 = (num ** 2 for num in range(1, user_number + 1))
for res_3 in square_gen_2:
    print(res_3, end=' ')

