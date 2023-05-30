import math
from typing import Optional
from abc import ABC


class MyMath(ABC):
    """
    Абстрактный класс MyMath с методами математических вычислений

    """
    @classmethod
    def circle_len(cls, radius: float) -> float:
        """
        Функция-метод вычисления длины окружности

        :param radius: радиус задаваемой окружности (int, float)
        :return: float
        """
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: float) -> float:
        """
        Функция-метод вычисления площади окружности

        :param radius: радиус задаваемой окружности (int, float)
        :return: float
        """
        return math.pi * radius ** 2

    @classmethod
    def cube_vol(cls, cube_side: float) -> float:
        """
        Функция-метод вычисления объёма куба

        :param cube_side: сторона задаваемого куба (int, float)
        :return: float
        """
        return cube_side ** 3

    @classmethod
    def sphere_sq(cls, radius: float) -> float:
        """
        Функция-метод вычисления площади сферы

        :param radius: радиус задаваемой сферы (int, float)
        :return: float
        """
        return 4 * math.pi * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_vol(cube_side=5)
res_4 = MyMath.sphere_sq(radius=6)
print(res_1)
print(res_2)
print(res_3)
print(res_4)