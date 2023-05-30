import random

class Human:

    def __init__(self, name, bellyful=50):
        self.name = name
        self.bellyful = bellyful
        self.house = House()

    def cube(self):
        number = random.randint(1, 6)
        if self.bellyful < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif number == 1:
            self.work()
        elif number == 2:
            self.eat()
        else:
            self.play()

    def eat(self):
        print(f'\n{self.name} ест и насыщается.')
        self.bellyful += 10
        self.house.food -= 10

    def work(self):
        print(f'\n{self.name} работает на работе.')
        self.bellyful -= 1
        self.house.money += 1

    def play(self):
        print(f'{self.name} играет и равзлекается.')
        self.bellyful -= 1

    def shopping(self):
        print(f'{self.name} пошел в магазин за продуктами.')
        self.house.food += 1
        self.house.money -= 1

    def info(self):
        print(('Человек - {}\n     Сытость - {}\n     Еда - {}\n     Деньги = {}\n').format(
            self.name, self.bellyful, self.house.food, self.house.money))
class House:

    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money

human_1 = Human('Адам')
human_2 = Human('Джек')

day_count = 0
while human_1.house.food != 0 or human_2.house.food != 0:
    day_count += 1
    print(f'\n****** День {day_count} ******\n')
    human_1.cube()
    human_2.cube()

if human_1.house.food == 0:
    print(f'\n{human_1.name} умер с голода.')
if human_2.house.food == 0:
    print(f'{human_2.name} умер с голода.')