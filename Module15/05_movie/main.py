films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

amount = int(input('Сколько фильмов хотите добавить? '))
favorite_list = []

for _ in range(amount):
    unavailable = True
    title = input('Введите название фильма: ')
    if title in films:
        favorite_list.append(title)
    else:
        print('Ошибка фильма', title, 'у нас нет :(')

print('Ваш список любимых фильмов:', end = ' ')
for film in favorite_list:
    print(film, end = ', ')