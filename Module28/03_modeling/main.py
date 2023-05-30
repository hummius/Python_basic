import math


class ValueMixin:
    """
    Класс-микс для расчета площади сторон 3д-фигуры
    """
    def square(self) -> float:
        result = 0
        for side in self.figure:
            result += side.square(self)
        return result


class Square:
    """
    Класс Квадрат, описывающий объект фигуры - квадрат.

    Args:
        side_length: длина стороны квадрата
    """
    def __init__(self, side_length: float) -> None:
        self._side_length = side_length

    @property
    def side_length(self) -> float:
        """
        Геттер для получения длины стороны квадрата

        :return: float
        """
        return self._side_length

    @side_length.setter
    def side_length(self, side_length: float) -> None:
        """
        Сеттер для внесения длины стороны квадрата

        :param side_length: внесенная длина стороны квадрата float
        :return: None
        """
        self._side_length = side_length

    def perimeter(self) -> float:
        """
        Функция вычисления периметра квадрата

        :return: float
        """
        return self.side_length * 4

    def square(self) -> float:
        """
        Функция вычисления площади квадрата

        :return: float
        """
        return self.side_length * self.side_length


class Triangle:
    """
    Класс Треугольник, описывающий фигуру - треугольник

    Args:
        base: длина основания треугольника
        height: высота треугольника
    """
    def __init__(self, base: float, height: float) -> None:
        self._base = base
        self._height = height

    @property
    def base(self) -> float:
        """
        Геттер для получения длины основания треугольника

        :return: float
        """
        return self._base

    @property
    def height(self) -> float:
        """
        Геттер для получения высоты треугольника

        :return: float
        """
        return self._height

    @base.setter
    def base(self, base: float) -> None:
        """
        Сеттер для внесения длины основания треугольника

        :param base: длина основания треугольника
        :return: None
        """
        self._base = base

    @height.setter
    def height(self, height: float) -> None:
        """
        Сеттер для внесения высоты треугольника

        :param height: высота треугольника
        :return: None
        """
        self._height = height

    def perimeter(self) -> float:
        """
        Функция вычисления периметра треугольника

        :return: float
        """
        return 2 * math.sqrt(self.height**2 + (self.base / 2)**2) + self.base

    def square(self) -> float:
        """
        Функция вычисления площади треугольника

        :return: float
        """
        return 0.5 * self.base * self.height


class Cube(Square, ValueMixin):
    """
    Класс Куб, описывающий трехмерную фигуру - куб

    Args:
        side_length: длина стороны квадрата

    Attributes:
        square: квадрат куба
        figure: список из квадратов
    """
    def __init__(self, side_length: float) -> None:
        super().__init__(side_length)
        self.square = Square
        self.figure = [self.square for _ in range(6)]


class Pyramid(Triangle, ValueMixin):
    """
    Класс Пирамида, описывающая трехмерную фигуру - пирамида

    Args:
        base: основание треугольника
        height: высота треугольника

    Attributes:
        square: квадрат пирамиды
        triangle: треугольник пирамиды
        figure: список фигур из которых состоит пирамида
    """
    def __init__(self, base: float, height: float) -> None:
        super().__init__(base, height)
        self.square = Square
        self.triangle = Triangle
        self.figure = [self.square]
        self.figure.extend([self.triangle for _ in range(4)])

