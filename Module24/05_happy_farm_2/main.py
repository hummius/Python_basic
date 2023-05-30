class Potato:
    grade_dict = {0: 'Посадка', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, number):
        self.number = number
        self.grade = 0

    def grow(self):
        if self.grade < 3:
            self.grade += 1
        self.print_state()

    def is_ripe(self):
        if self.grade == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(self.number, Potato.grade_dict[self.grade]))



class PotatoGarden:

    def __init__(self, count, care_status=False, grow_status=False):
        self.potatoes = [Potato(number) for number in range(1, count + 1)]
        self.name = 'грядка картошки'
        self.care_status = care_status
        self.grow_status = grow_status

    def grow_all(self):
        if self.care_status:
            print('\nКартошка прорастает!\n')
            for potat in self.potatoes:
                potat.grow()
            self.care_status = False
        else:
            print('\nКартошка не будет расти, если за ней не ухаживать.')
    def are_all_ripe(self):
        if not all([potat.is_ripe() for potat in self.potatoes]):
            print('Картошка еще не созрела\n')
        else:
            print('Вся картошка созрела. Можно собирать!\n')
            self.grow_status = True

class Gardener:

    def __init__(self, name, garden):
        self.name = name
        self.garden = garden
        self.harvest = list()

    def care(self):
        print(f'\n{self.name} ухаживает и поливает {my_garden.name}.')
        my_garden.care_status = True

    def ingathering(self):
        if my_garden.grow_status == True:
            for potat in my_garden.potatoes:
                print(f'{gardener.name} собирает картошку {potat.number}')
                self.harvest.append('картошка')

my_garden = PotatoGarden(5)
gardener = Gardener('Альфред', my_garden)
my_garden.are_all_ripe()
gardener.care()
for _ in range(3):
    gardener.care()
    my_garden.grow_all()
my_garden.are_all_ripe()
gardener.ingathering()

print(f'\nУрожай {gardener.name}a: {gardener.harvest}')