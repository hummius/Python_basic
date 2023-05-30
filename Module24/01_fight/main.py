import random

class Unit:

    def __init__(self, index):
        self.name = f'Воин *{str(index)}*'
        self.health = 100

    def fight(self, unit_2):
        while True:
            if unit_2.health_check() or unit_1.health_check():
                break
            else:
                initiative = random.randint(1, 2)
                if initiative == 1:
                    print(f'\n{unit_1.name} бьёт по {unit_2.name}')
                    unit_2.health -= 20
                    print(f'{unit_2.name} получает урон -20')
                else:
                    print(f'\n{unit_2.name} бьёт по {unit_1.name}')
                    unit_1.health -= 20
                    print(f'{unit_1.name} получает урон -20')

    def health_check(self):
        if unit_1.health == 0 or unit_2.health == 0:
            return True
    def who_is_win(self, unit_2):
        if unit_1.health > unit_2.health:
            print(f'\n{unit_1.name} выиграл в битве.')
        else:
            print(f'\n{unit_2.name} выиграл в битве.')

unit_1 = Unit(1)
unit_2 = Unit(2)

print(unit_1.name, unit_1.health)

unit_1.fight(unit_2)
unit_1.who_is_win(unit_2)