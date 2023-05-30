def line_checking(line_for_check):
    try:
        line_list = line_for_check.split()
        if len(line_list) < 3:
            raise Exception
        if not line_list[0].isdigit() or not line_list[2].isdigit():
            raise Exception
        if not '+' and not '-' and not '*' and not '/' in line_list[1] or len(line_list[1]) > 1:
            raise Exception

    except Exception:
        print(f'Обнаружена ошибка в строке: {line_for_check}', end='   ')
        answer = input('Хотите исправить? ').lower()
        if answer == 'да':
            return line_fixer()
        if answer == 'нет':
            return False
        else:
            print('Ошибка: не правильно дана команда.')
    else:
        return line_for_check

def line_fixer():
    fix_line = input('Введите исправленную строку: ')
    return line_checking(fix_line)

def calculating(line_for_calc):
    calc_list = line_for_calc.split()

    if calc_list[1] == '+':
        result = int(calc_list[0]) + int(calc_list[2])
    elif calc_list[1] == '-':
        result = int(calc_list[0]) - int(calc_list[2])
    elif calc_list[1] == '*':
        result = int(calc_list[0]) * int(calc_list[2])
    elif calc_list[1] == '/':
        result = int(calc_list[0]) / int(calc_list[2])

    return result


with open('calc.txt', 'r', encoding='utf-8') as file:
    summ = 0

    for line in file.readlines():
        checked_line = line_checking(line)
        if checked_line:
            summ += calculating(checked_line)

print(f'\nСумма результатов: {summ}')