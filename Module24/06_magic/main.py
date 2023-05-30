class Fire:
    name = 'Огонь'

    def __add__(self, other):
        if other.name == 'Вода':
            return Steam()
        elif other.name == 'Воздух':
            return Lightning()
        elif other.name == 'Земля':
            return Lava()
        else:
            return None

class Water:
    name = 'Вода'

    def __add__(self, other):
        if other.name == 'Воздух':
            return Storm()
        elif other.name == 'Огонь':
            return Steam()
        elif other.name == 'Земля':
            return Dirt()
        else:
            return None
class Air:
    name = 'Воздух'

    def __add__(self, other):
        if other.name == 'Вода':
            return Storm()
        elif other.name == 'Огонь':
            return Lightning()
        elif other.name == 'Земля':
            return Dust()
        else:
            return None

class Earth:
    name = 'Земля'


class Storm:
    name = 'Шторм'

    def __add__(self, other):
        if other.name == 'Вода':
            return Dirt()
        elif other.name == 'Воздух':
            return Dust()
        elif other.name == 'Огонь':
            return Lava()

class Steam:
    name = 'Пар'

class Dirt:
    name = 'Грязь'

class Lightning:
    name = 'Молния'

class Dust:
    name = 'Пыль'

class Lava:
    name = 'Лава'

class Snow:
    name = 'Снег'

    def __add__(self, other):
        if other.name == 'Вода':
            return Ice()
        elif other.name == 'Огонь':
            return Water()
        elif other.name == 'Воздух':
            return Snowfall()
        elif other.name == 'Земля':
            return Snowdrift()

class Ice:
    name = 'Лёд'

class Snowfall:
    name = 'Снегопад'

class Snowdrift:
    name = 'Сугроб'


a = Fire()
b = Water()

c = a + b
print(c.name)