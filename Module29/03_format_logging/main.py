from collections.abc import Callable
from datetime import datetime
import functools
import time


def log_methods(date: str) -> Callable:
    """
    Декоратор класса

    :param date: введенный формат для вывода времени и даты
    :return:
    """
    def dec_log(cls):
        for method in dir(cls):
            if method.startswith('__') is False:
                cur_method = getattr(cls, method)
                dec_method = timer(cls, cur_method, date)
                setattr(cls, method, dec_method)

        return cls
    return dec_log

def timer(cls: Callable, func: Callable, date: str) -> Callable:
    """
    Декоратор выводящий время, дату выполнения и затраченное время
    :param cls: класс декорируемой функции
    :param func: декорируемая функция
    :param date: принимаемый формат вывода даты и времени
    :return:
    """
    @functools.wraps(cls)
    def wrapped(*args, **kwargs):
        format_date = date
        for symbol in format_date:
            if symbol.isalpha():
                format_date = format_date.replace(symbol, '%' + symbol)
        print(f"- Запускается '{cls.__name__}.{func.__name__}'. "
              f"Дата и время запуска: {datetime.now().strftime(format_date)}")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"- Завершение '{cls.__name__}.{func.__name__}', время работы = {round(end - start, 3)}s ")

        return cls
    return wrapped



@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
