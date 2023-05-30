import functools
import time
from typing import Callable


def delay(func: Callable) -> Callable:
    """
    Декоратор задерживающий выполнение декорируемой функции

    :param func: декорируемая функция
    :return:
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        time.sleep(10)
        result = func(*args, **kwargs)
        return result

    return wrapped_func


@delay
def test() -> None:
    """
    Функция для теста декоратора

    :return: None
    """
    print('<Тут что-то происходит...>')


test()
