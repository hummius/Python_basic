import random
class KillError(Exception):
    def __str__(self):
        return 'Вы убили невинного жука.'

class DrunkError(Exception):
    def __str__(self):
        return 'Вы выпили много алкоголя.'
class CarCrashError(Exception):
    def __str__(self):
        return 'Вы попали в небольшую аварию.'
class GluttonyError(Exception):
    def __str__(self):
        return 'Вы слишком объелись'
class DepressionError(Exception):
    def __str__(self):
        return 'Вы впали в уныние.'


class Person:
    """
    Класс Человек, описывающий пользователя.

    :param:
        __name: имя
        __enlightenment: статус просветления
        __karma: количество баллов кармы
    """
    def __init__(self, name):
        self.__name = name
        self.__enlightenment = False
        self.__karma = 0

    def get__name(self):
        """
        Геттер для получения имени

        :return: __name
        :rtype: str
        """
        return self.__name

    def get__karma(self):
        """
        Геттер для получения количества кармы

        :return: __karma
        :rtype: int
        """
        return self.__karma

    def set__karma(self, scores):
        """
        Сеттер для установления кармы

        :param scores: подаваемое количество кармы
        :return: прибавляет подаваемое количество кармы к общей сумме
        """
        self.__karma += scores

    def set__enlightenment(self, arg):
        """
        Сеттер для установления статуса "просветления"

        :param arg: True или False
        :return: измененный статус "просветления"
        """
        self.__enlightenment = arg

    def get__enlightenment(self):
        """
        Геттер для получения статуса "просветения"

        :return: __enlightenment
        """
        return self.__enlightenment

def one_day(person):
    day = 0
    while True:
        try:
            day += 1
            print(f'\nДень {day}')
            if random.randrange(1, 11) == 6:
                raise random.choice([KillError, DrunkError, CarCrashError,
                                     GluttonyError, DepressionError])
            else:
                new_karma = random.randint(1, 7)
                person.set__karma(new_karma)
                print(f'Карма за этот день - {new_karma}')

        except Exception as exc:
            print(exc)
            with open('karma.log', 'a', encoding='utf-8') as file:
                file.write(f'День - {day}   Личность: {person.get__name()}\n {type(exc)}\n {exc}\n\n')
        finally:
            if person.get__karma() >= 500:
                person.set__enlightenment(True)
                break
    if person.get__enlightenment():
        print('\nПросветление достигнуто!')

me = Person(input('Введите имя: '))
one_day(me)
