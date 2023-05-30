import random

class House:
    """
    Класс Дом, содержащий в себе характеристики обеспеченности дома

    Attributes:
        money: количество денег
        food: количество пищи
        cat_food: количество пищи для кота
        dirt: загрязненность дома
    """
    def __init__(self):
        self.money = 100
        self.food = 50
        self.cat_food = 30
        self.dirt = 0

class Family:
    """
    Класс Семья, описывающий в себе членов семьи

    Args:
        name (str): Имя члена семьи

    Attributes:
        satiety: сытость члена семьи
        money_total: общее количество заработанных денег
        food_total: общее количество съеденной еды
        fur_coat_total: общее количество купленных шуб
    """
    money_total = 0
    food_total = 0
    fur_coat_total = 0
    house = House()

    def __init__(self, name):
        self.name = name
        self.satiety = 30

    def __str__(self):
        return f'\n\nЗаработано денег за год: {self.money_total}\n' \
               f'Еды съедено за год: {self.food_total}\n' \
               f'Куплено шуб за год: {self.fur_coat_total}'

    def eat(self):
        """
        Функция-метод приема пищи для членов семьи

        :return: self.satiety += 30
                self.house.food -= 30
                Family.food_total += 30
        """
        self.satiety += 30
        self.house.food -= 30
        Family.food_total += 30
        print(f'{self.name} ест.')

    def status_check(self):
        """
        Функция-метод для сверки состояния сытости членов семьи

        :return: True
        """
        if self.satiety < 0:
            print(f'{self.name} умер. от голода')
            return True


class Child(Family):
    """
    Класс Ребенок, описывающий ребенка семьи

    Args:
        name: имя ребенка

    Attributes:
        happiness: состояние счастья
    """
    def __init__(self, name):
        super().__init__(name)
        self.happiness = 100

    def play_games(self):
        """
        Функция-метод для игры ребенка

        :return: happiness += 10
                 satiety -= 10
        """
        print(f'{self.name} играет с игрушками.')
        self.happiness += 10
        self.satiety -= 10

    def eat(self):
        """
        Функция-метод приема пищи для ребенка

        :return: satiety += 15
                 house.food -= 15
                 Family.food_total += 15
        """
        self.satiety += 15
        self.house.food -= 15
        Family.food_total += 15
        print(f'{self.name} ест.')

    def petting(self):
        """
        Функция-метод поглаживания кота для ребенка

        :return: happiness += 5
                 satiety -= 10
        """
        self.happiness += 5
        self.satiety -= 10
        print(f'{self.name} гладит кота')

    def status_check(self):
        """
        Функция-метод сверки состояния счастья и сытости ребенка

        :return: True
        """
        super().status_check()
        if self.happiness < 10:
            print(f'{self.name} умер от депрессии')
            return True

    def cube(self):
        """
        Функция-метод рандомизации занятости ребенка

        :return:
        """
        number = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.happiness < 20:
            self.play_games()
        elif number == 2:
            self.eat()
        else:
            self.petting()
class Husband(Family):
    """
    Класс Муж, описывающий члена семьи в статусе мужа

    Args:
        name: имя мужа

    Attributes:
        happiness: состояние счастья

    """
    def __init__(self, name):
        super().__init__(name)
        self.happiness = 100

    def status_check(self):
        """
        Функция-метод сверки состояния счастья и сытости мужа

        :return: True
        """
        super().status_check()
        if self.happiness < 10:
            print(f'{self.name} умер от депрессии')
            return True

    def eat(self):
        """
        Функция-метод приема пищи для мужа

        :return:
        """
        if self.house.food > 30:
            super().eat()
        else:
            print(f'{self.name} не может поесть так как еды нету. {self.house.food}')
            self.work()


    def play_comp(self):
        """
        Функция-метод игры в компьютер для мужа

        :return: happiness += 20
                 satiety -= 10
        """
        self.happiness += 20
        self.satiety -= 10
        print(f'{self.name} играет в компьютер.')
    def work(self):
        """
        Функция-метод работы для мужа

        :return: house.money += 150
                 satiety -= 10
                 happiness -= 10
                 Family.money_total += 150
        """
        self.house.money += 150
        self.satiety -= 10
        self.happiness -= 10
        Family.money_total += 150
        print(f'{self.name} вернулся и положил деньги в тумбочку. Деньги: {self.house.money}')

    def petting(self):
        """
        Функция-метод поглаживания кота для мужа

        :return: happiness += 5
                 satiety -= 10
        """
        self.happiness += 5
        self.satiety -= 10
        print(f'{self.name} гладит кота')


    def cube(self):
        """
        Функция-метод рандомизации занятости мужа

        :return:
        """
        number = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.house.money < 150:
            self.work()
        elif self.happiness < 30:
            self.play_comp()
        elif number == 1:
            self.play_comp()
        elif number == 2:
            self.eat()
        else:
            self.petting()

class Wife(Family):
    """
    Класс Жена, описывающий члена семьи в статусе жены

    Args:
        name: имя жены

    Attributes:
        happiness: состояние счастья жены
    """
    def __init__(self, name):
        super().__init__(name)
        self.happiness = 100

    def status_check(self):
        """
        Функция-метод дл сверки состояния сытости и счастья жены

        :return: True
        """
        super().status_check()
        if self.happiness < 10:
            print(f'{self.name} умерла от депрессии.')
            return True

    def eat(self):
        """
        Функция-метод приема пищи для жены

        :return:
        """
        if self.house.food > 30:
            super().eat()
        else:
            print(f'{self.name} не может поесть так как еды нету.{self.house.food}')
            self.shopping()

    def shopping(self):
        """
        Функция-метод похода в магазин за продуктами для жены

        :return:
        """
        self.satiety -= 10
        if self.house.money > 90:
            self.house.food += 60
            self.house.money -= 60
        if self.house.cat_food < 50:
            self.house.cat_food += 30
            self.house.money -= 30
            print(f'{self.name} идет в магазин и покупает еду.')
        else:
            print(f'{self.name} не хватает денег для похода в магазин.')
            self.satiety += 10

    def fur_coat(self):
        """
        Функция-метод покупки шубы для жены

        :return: satiety -= 10
                 house.money -= 350
                 happiness += 60
                 Family.fur_coat_total += 1
        """
        self.satiety -= 10
        self.house.money -= 350
        self.happiness += 60
        Family.fur_coat_total += 1
        print(f'{self.name} идет в магазин и покупает шубу')

    def petting(self):
        """
        Функция-метод поглаживания кота для жены

        :return: happiness += 5
                 satiety -= 10
        """
        self.happiness += 5
        self.satiety -= 10
        print(f'{self.name} гладит кота')
        print(self.happiness)

    def cube(self):
        """
        Функция-метод для рандомизации занятости жены

        :return:
        """
        number = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.house.food < 60 or self.house.cat_food < 20:
            self.shopping()
        elif self.happiness < 20:
            self.fur_coat()
        elif self.house.dirt > 90:
            self.cleaning()
        elif number == 1:
            self.cleaning()
        elif number == 2:
            self.eat()
        else:
            self.petting()

    def cleaning(self):
        """
        Функция-метод уборки дома для жены
        :return:
        """
        print(f'{self.name} убралась в доме')
        self.satiety -= 10
        self.happiness -= 10
        if self.house.dirt < 100:
            self.house.dirt -= self.house.dirt
        else:
            self.house.dirt -= 100
class Cat(Family):
    """
    Класс Кот, описывающий члена семьи - кота

    Args:
        name: кличка кота
    """
    def __init__(self, name):
        super().__init__(name)

    def status_check(self):
        super().status_check()

    def eat(self):
        """
        Функция-метод приема пищи для кота

        :return:
        """
        if self.house.cat_food > 0:
            self.satiety += 20
            self.house.cat_food -= 10
            Family.food_total += 10
            print(f'{self.name} кушает.')
        else:
            print(f'{self.name} не может по есть так как еды нету.')
            self.tear_wallpaper()
    def tear_wallpaper(self):
        """
        Функция-метод раздирания обоев для кота

        :return: house.dirt += 5
                 satiety -= 10
        """
        print(f'{self.name} дерет обои')
        self.house.dirt += 5
        self.satiety -= 10

    def sleep(self):
        """
        Функция-метод сна для кота

        :return: satiety -= 10
        """
        print(f'{self.name} спит.')
        self.satiety -= 10

    def cube(self):
        """
        Функция-метод рандомизации занятости кота

        :return:
        """
        number = random.randint(1, 3)
        if self.satiety < 20:
            self.eat()
        elif number == 1:
            self.tear_wallpaper()
        elif number == 2:
            self.eat()
        else:
            self.sleep()


def start_game():
    husband = Husband('Френк')
    wife = Wife('Марта')
    child = Child('Барт')
    cat_1 = Cat('Барсик')
    cat_2 = Cat('Пушок')
    cat_3 = Cat('Кисель')
    day = 0
    while True:
        day += 1
        print(f'\n**День {day}**')
        if Family.house.dirt > 90:
            child.happiness -= 10
            husband.happiness -= 10
            wife.happiness -= 10
        Family.house.dirt += 5
        husband.cube()
        wife.cube()
        child.cube()
        cat_1.cube()
        cat_2.cube()
        cat_3.cube()
        if wife.status_check() or husband.status_check() or cat_1.status_check()\
                or cat_2.status_check() or cat_3.status_check():
            break
        if day == 365:
            print(Family.__str__(Family))
            break

start_game()