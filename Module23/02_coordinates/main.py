import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x

try:
    with open('coordinates.txt', 'r', encoding='utf-8') as file:
        for line in file:
            nums_list = line.split()
            try:
                res1 = f(int(nums_list[0]), int(nums_list[1]))
            except ZeroDivisionError:
                res1 = f(int(nums_list[0]), int(nums_list[1]))
                print('Ошибка: в функции 1 произошло деление на ноль. Функция перезапускается')
            try:
                res2 = f2(int(nums_list[0]), int(nums_list[1]))
            except ZeroDivisionError:
                res2 = f2(int(nums_list[0]), int(nums_list[1]))
                print('Ошибка: в функции 2 произошло деление на ноль. Функция перезапускается')
            number = random.randint(0, 100)

            with open('result.txt', 'a', encoding='utf-8') as file_2:
                file_2.write("+{:-^19}+\n".format('+'))
                my_list = sorted([str(res1), str(res2), str(number)])
                file_2.write(f"{' '.join(my_list)}\n")

except FileNotFoundError:
    print('Файл coordinates.txt не найден.')
except (ValueError, IndexError):
    print('Ошибка: не соответствующие данные в файле')
else:
    print('Программа завершилась успешно. Данные вписаны в файл result.txt')