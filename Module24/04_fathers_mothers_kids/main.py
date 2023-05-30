class Parent:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = list()
        number = int(input('Сколько детей у родителя? '))
        for _ in range(number):
            try:
                name = input('Имя ребенка: ')
                age = int(input('Возраст ребенка: '))
                if self.age > age + 16:
                    self.children.append(Child(name, int(age)))
                else:
                    print('Ошибка: ребенок должен быть младше, минимум на 16 лет.')
            except ValueError:
                print('Ошибка: введены не верные данные.')

    def parent_info(self):
        print('\nМеня зовут - {}\nМой возраст - {}\nУ меня есть дети:'.format(
            self.name, self.age), end=' ')
        for kid in self.children:
            print(kid.name, end=' ')
            print()
    def calm_down(self):
        for child in self.children:
            answer = input(f'Успокоить {child.name} (да/нет)? ').lower()
            if answer == 'да':
                if child.calm_status == False:
                    print(f'\n{self.name} успокаивает {child.name}')
                    child.calm_status = True
                else:
                    print('\nРебенка не нужно успокаивать, он и так ведет себя спокойно.')

    def feed(self):
        for child in self.children:
            answer = input(f'Покормить {child.name} (да/нет)? ').lower()
            if answer == 'да':
                if child.hungry_status == False:
                    print(f'\n{self.name} кормит {child.name}')
                    child.hangry_status = True
                else:
                    print('\nРебенок не хочет есть.')

class Child:

    def __init__(self, name, age, calm_status=False, hungry_status=False):
        self.name = name
        self.age = age
        self.calm_status = calm_status
        self.hungry_status = hungry_status

parent_1 = Parent('Ольга', 45)
parent_1.parent_info()
parent_1.calm_down()
parent_1.feed()