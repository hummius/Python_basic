from typing import Callable, Optional


def debug(func: Callable) -> Callable:
    """
    Декоратор выводит имя декорируемой функции (вместе со всеми передаваемыми аргументами),
    а затем — какое значение она возвращает.

    :param func: декорируемая функция
    :return: Callable
    """

    def wrapped_func(*args, **kwargs) -> None:
        print(f'Вызывается функция {func.__name__}{args}{kwargs}')
        print(f'{repr(func.__name__)} вернула значение {repr(func(*args, **kwargs))}')
        result = f'{func(*args, **kwargs)}\n'
        return print(result)

    return wrapped_func

@debug
def greeting(name: str, age=None) -> str:
    """
    Функция возвращающая строку-шаблон с вводимыми данными.

    :param name: имя
    :param age: возраст
    :return: str
    """
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)

greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)