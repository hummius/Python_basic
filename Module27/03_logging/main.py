import functools
from typing import Callable
import datetime


def logging(func: Callable) -> Callable:
    """
    Декоратор для вывода имени, документации декорируемой функции в консоль,
    а так же логирования ошибок в лог файл.

    :param func: декорируемая функция
    :return: Callable
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> None:
        print(func.__name__)
        print(func.__doc__)
        try:
            func(*args, **kwargs)
        except BaseException as exc:
            with open('function_errors.log', 'a', encoding='utf-8') as file:
                file.write(f'{datetime.datetime.now()} {type(exc)} {exc}\n')

    return wrapped_func


@logging
def square_sum() -> int:
    """
    Функция для теста декоратора

    :return: int
    """
    number = 'fd'
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])
    return result

res = square_sum()
print(res)
