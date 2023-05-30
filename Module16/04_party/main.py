guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
    command = input('Гость пришёл или ушёл? ')
    if command == 'пришёл':
        name = input('Имя гостя: ')
        if len(guests) < 6:
            print('Привет,', name)
            guests.append(name)
        else:
            print('Прости,', name + ', но мест нет.')
    elif command == 'ушёл':
        name = input('Имя гостя: ')
        print('Пока,', name + '!')
        guests.remove(name)
    elif command == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    else:
        print('Ошибка: не существующая команда.')

