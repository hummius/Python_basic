import random

class Student:

    def __init__(self, name):
        self.name = name
        self.group_number = random.randint(1, 3)
        self.progress = [random.randint(20, 100), random.randint(20, 100),
                                         random.randint(20, 100), random.randint(20, 100),
                                         random.randint(20, 100)]

class Students_class:

    def __init__(self, list):
        self.students_list = [Student(name) for name in list]

    def print(self):
        print('Список студентов: ')
        for i in self.students_list:
            print(i.name, i.group_number, i.progress)

    def sorted_list(self):
        new_list = sorted(self.students_list, key=lambda x: sum(x.progress) / 5)
        print('\n\n')
        for i in new_list:
            print(i.name, i.group_number, (sum(i.progress) / 5))



students = Students_class(['Иван Иванов', 'Петр Опухов', 'Оксана Кочеткова', 'Фёдор Николаев', 'Тимофей Андреев',
                        'Дмитрий Осипов', 'Фёдор Сумкин', 'Алексей Морозов', 'Сергей Ухов', 'Павел Петров'])

students.print()
students.sorted_list()