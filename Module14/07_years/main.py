start_year = int(input('Введите первый год: '))
fin_year = int(input('Введите второй год: '))

if start_year > fin_year or start_year < 1000:
    print('Ошибка: не верно введены данные.')
else:
    print('Годы от', start_year, 'до', fin_year, 'с тремя одинаковыми цифрами:')
    for year in range (start_year, fin_year + 1):
        temp = year
        prev_number = year % 10
        amount = 0
        while temp != 0:
            number = temp % 10
            temp //= 10
            if prev_number == number:
                amount += 1
        if amount == 3:
            print(year)