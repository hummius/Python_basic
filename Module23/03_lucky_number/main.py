import random

def lucky_number():
    total_number = 0
    while True:
        try:
            number = int(input('Введите число: '))
            fatal_number = random.randint(1, 13)
            if fatal_number == 13:
                raise Exception('Вас постигла неудача!')
        except Exception as exc:
            print(exc)
            break

        else:
            total_number += number
            with open('out_file.txt', 'a', encoding='utf-8') as data_file:
                data_file.write(str(number) + '\n')
            if total_number >= 777:
                print('Вы успешно выполнили условие для выхода из порочного цикла!')
                break

lucky_number()