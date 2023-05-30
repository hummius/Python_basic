import functools
from collections.abc import Callable


def callback(path: str) -> Callable:
    """
    Декоратор функции обратного вызова

    :param path: вводимый путь
    :return: Callable
    """
    def dec_callback(func: Callable) -> Callable:
        app[path] = func

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper
    return dec_callback


app = dict()


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
