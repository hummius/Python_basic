from typing import Callable


def counter(func: Callable) -> Callable:
    """
    Декоратор - счетчик количества вызовов декорируемой функции.

    :param func: декорируемая функция
    :param lst: список для хранения данных о подсчетах

    :return: Callable
    """

    def wrapped_func(*args, **kwargs):
        func(*args, **kwargs)
        wrapped_func.count += 1
        result = f'Количество вызовов функции {func.__name__}: {wrapped_func.count}'
        return print(result)

    wrapped_func.count = 0
    return wrapped_func


@counter
def test() -> None:
    """
    Функция для теста
    :return: None
    """
    return


test()
test()
test()
test()
