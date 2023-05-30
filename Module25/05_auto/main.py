import math

class Automobile:
    """
    Класс Автомобиль, описывающий координаты и направление автомобиля

    Args:
        x и y (float): координаты
        i (float): направление

    """
    def __init__(self, x, y, i):
        self.x = x
        self.y = y
        self.i = i

    def move(self, dist):
        """
        Функция для движения объекта

        :param dist: расстояние
        :return: новые координаты X и Y
        """
        self.x = self.x + dist * math.cos(self.i)
        self.y = self.y + dist * math.sin(self.i)

    def __str__(self):
        return f'\nКоординаты:\n' \
               f'   X: {self.x} Y: {self.y}\n' \
               f'Направление: {self.i}'

class Bus(Automobile):
    """
    Класс Автобус, описывающий параметры автобуса

    Args:
        x и y (float): координаты
        i (float): угол направления
        passengers (int): количество пассажиров
    """
    def __init__(self, x, y, i, passengers):
        super().__init__(x, y, i)
        self.passengers = passengers
        self.money_amount = 0

    def move(self, dist):
        self.money_amount += 1 * self.passengers * dist
        super().move(dist)

    def enter_pass(self, amount):
        """
        Функция посадки новых пассажиров в автобус

        :param amount: кол-во пассажиров
        :return: passengers + amount
        """
        print(f'В автобус зашло {amount} человек')
        self.passengers += amount

    def exit_pass(self, amount):
        """
        Функция высадки пассажиров из автобуса

        :param amount: кол-во пассажиров
        :return: passengers - amount
        """
        print(f'Из автобуса вышло {amount} человек')
        self.passengers -= amount

    def __str__(self):
        print(super().__str__())
        return f'Количество денег заработано: {round(self.money_amount, 2)}\n' \
               f'Количество пассажиров в автобусе: {self.passengers}'

auto_1 = Automobile(0.12344, 1.42453, 45)
print(auto_1)
auto_1.move(3)
print(auto_1)
autobus_1 = Bus(0.12344, 1.42453, 45, 20)
print(autobus_1)
autobus_1.move(3)
print(autobus_1)
autobus_1.enter_pass(3)
autobus_1.exit_pass(5)
print(autobus_1)