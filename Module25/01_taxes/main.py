class Property:
    """
    Базовый класс, описывающий собственность

    __taxes_sum: сумма насчитанного налога на всю недвижимость

    Args:
        worth (int): стоимость недвижимости
    """
    __taxes_sum = 0

    def __init__(self, worth):
        self.__worth = worth

    def tax_count(self, tax):
        """
        Метод расчета налога и суммирования полученных данных от дочерних классов

        Arg:
            tax (int): индивидуальный делитель для расчета налога
        """
        Property.__taxes_sum += self.__worth / tax

    def __str__(self):
        """Метод для вывода суммы налога"""
        return f'{self.__taxes_sum}'

    def get_worth(self):
        """
        Геттер для получения стоимости

        :return: __worth
        :rtype: int
        """
        return self.__worth

    def get_tax_sum(self):
        """
        Геттер для получения суммы налога

        :return: __taxes_sum
        :rtype: int
        """
        return self.__taxes_sum


class Apartment(Property):
    """
    Класс Квартира.

    """

    def tax_count(self, tax=1000):
        super().tax_count(tax)


class Car(Property):
    """
    Класс Машина.

    """
    def tax_count(self, tax=200):
        super().tax_count(tax)


class CountryHouse(Property):
    """
    Класс Дача.

    """
    def tax_count(self, tax=500):
        super().tax_count(tax)


def start_taxes_count():
    money = int(input('Количество денег: '))
    my_apartment = Apartment(int(input('Стоимость квартиры: ')))
    my_car = Car(int(input('Стоимость машины: ')))
    my_country_house = CountryHouse(int(input('Стоимость дачи: ')))

    my_apartment.tax_count()
    my_car.tax_count()
    my_country_house.tax_count()


    if money < Property.get_tax_sum(Property):
        print(Property.__str__(Property))
        print(f'Для уплаты налога вам не хватает: {abs(money - Property.get_tax_sum(Property))}')
    else:
        print('Денег хватает для уплаты налога')


start_taxes_count()
