from collections.abc import Callable
import functools


def decorator_with_args_for_any_decorator(decorator) -> Callable:
    """
    Декоратор помогающий декорируемому декоратору получать произвольные аргументы

    :param decorator: декорируемый декоратор
    :return: Callable
    """
    def decorator_maker(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable) -> Callable:
            return decorator(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker
@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:
    """
    Декоратор вывода переданных аргументов
    :param func: декорируемая функция
    :param dec_args: аргументы
    :param dec_kwargs: аргументы
    :return:
    """
    @functools.wraps(func)
    def wrapped(*func_args, **func_kwargs):
        print('Переданные арги и кварги в декоратор:', dec_args, dec_kwargs)
        return func(*func_args, **func_kwargs)
    return wrapped


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
