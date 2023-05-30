from _collections_abc import Iterable


def q_hofstadter(lst: list[int]) -> Iterable[list]:
    """
    Функция-генератор последовательности Q Хофштадтера

    :param lst: список чисел на вход

    :return:
    """
    if lst[1] == 2:
        return
    while True:
        try:
            q = lst[-lst[-1]] + lst[-lst[-2]]
            lst.append(q)
            yield q
        except IndexError:
            return


for index, number in enumerate(q_hofstadter([1, 1])):
    if index <= 30:
        print(number, end=', ')
    else:
        break
