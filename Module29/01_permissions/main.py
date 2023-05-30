import functools
from collections.abc import Callable


def check_permission(login: str) -> Callable:
    """
    Декоратор с аргументом для проверки допуска вводимого логина к функции

    :param login: вводимый логин

    :return: Callable
    """
    def check(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if login in user_permissions:
                    return func(*args, **kwargs)
                raise PermissionError
            except PermissionError:
                print('PermissionError: у пользователя недостаточно прав.')

            return True

        return wrapper

    return check


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
