from typing import Callable
import functools


def how_are_you(func: Callable) -> Callable:
    """
    Декоратор-шутка выводящая сначала вопрос,
    а после ответа запускает декорируемую функцию

    :param func: функция для запуска
    """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> None:
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        result = func(*args, **kwargs)
        return result

    return wrapped_func


@how_are_you
def test() -> None:
    """
    Функция для теста декоратора

    :return: None
    """
    print('<Тут что-то происходит...>')


test()
