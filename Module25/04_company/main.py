class Person:
    """
    Базовый класс, описывающий человека

    Args:
        name: имя
        surname: фамилия
        age: возраст
    """
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        """
        Геттер для получения имени

        :return: __name
        """
        return self.__name

    def get_surname(self):
        """
        Геттер для получения фамилии

        :return: __surname
        """
        return self.__surname

class Employee(Person):
    """
    Класс Работник

    """

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
    def payroll(self):
        """
        Метод расчета заработной платы

        :return:
        """
        return self
class Manager(Employee):
    """
    Класс Менеджер, описывающий работника на должности менеджера

    :param: salary (int): заработная плата менеджера

    """
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.salary = 13000

    def payroll(self):
        return self.salary
    def __str__(self):
        return f'Manager {self.get_name()} {self.get_surname()} заработная плата: {self.payroll()}\n'
class Agent(Employee):
    """
    Класс Агент, описывающий работника на должности агента

    Args:
        sales_volume (int): объемы продаж

    :param: salary: заработная плата
    """
    def __init__(self, name, surname, age, sales_volume):
        super().__init__(name, surname, age)
        self.salary = 5000
        self.sales_volume = sales_volume

    def __str__(self):
        return f'Agent {self.get_name()} {self.get_surname()} заработная плата: {round(self.payroll())}\n'

    def payroll(self):
        return self.salary + (self.sales_volume / 100) * 5

class Worker(Employee):
    """
    Класс Рабочий, описывающий обычного рабочего

    Args:
        hours (int): отработанные часы рабочего
    """
    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.hours = hours

    def __str__(self):
        return f'Worker {self.get_name()} {self.get_surname()} заработная плата: {self.payroll()}\n'

    def payroll(self):
        return 100 * self.hours


manager_1 = Manager('Юрий', 'Доронин', 35)
manager_2 = Manager('Алина', 'Дмитриева', 35)
manager_3 = Manager('Василий', 'Петров', 37)
agent_1 = Agent('Андрей', 'Николаев', 33, 400000)
agent_2 = Agent('Ольга', 'Василькина', 41, 600000)
agent_3 = Agent('Денис', 'Верзилов', 33, 800000)
worker_1 = Worker('Алексей', 'Иванов', 27, 160)
worker_2 = Worker('Пётр', 'Паханов', 25, 137)
worker_3 = Worker('Сергей', 'Стаханов', 23, 180)

print('', manager_1,
manager_2,
manager_3,
agent_1,
agent_2,
agent_3,
worker_1,
worker_2,
worker_3,
end='\t')