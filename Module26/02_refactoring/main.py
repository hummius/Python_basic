from typing import List


def gen(lst_1: List[int], lst_2: List[int], number: int) -> str:
    """
    Функция-генератор

    :param lst_1: список с цифрами
    :param lst_2: список с цифрами
    :param number: сумма которую при умножении нужно получить
    :return: x * y = result
    """
    for x in lst_1:
        for y in lst_2:
            result = x * y
            yield f'{x} * {y} = {result}'
            if result == number:
                print('Found!!!')
                return


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56
for res in gen(list_1, list_2, to_find):
    print(res)
