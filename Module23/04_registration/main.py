def line_checking(line_for_check):
    try:
        if len(line_for_check.split()) < 3:
            raise IndexError('Не присутствуют все три поля')
        if not line_for_check.split()[0].isalpha():
            raise NameError('Поле "Имя" содержит не только буквы')
        if not '@' in line_for_check.split()[1] and not '.' in line.split()[1]:
            raise SyntaxError('Поле "Имейл" не содержит @ и .(точку)')
        if not int(line_for_check.split()[2]) > 9 or not int(line_for_check.split()[2]) < 99:
            raise ValueError('Поле "Возраст" не является числом от 10 до 99')
    except (IndexError, NameError, SyntaxError, ValueError) as exc:
        return False, exc
    else:
        return True, 'ok'

def bad_sort(bad_line, argument):
    with open('registrations_bad.log', 'a', encoding='utf-8') as bad_file:
        bad_file.write(f'{bad_line[0:len(bad_line) - 1]}          {str(argument)}\n')

def good_sort(good_line):
    with open('registrations_good.log', 'a', encoding='utf-8') as good_file:
        good_file.write(good_line)

with open('registrations.txt', 'r', encoding='utf-8') as file:
    for line in file:
        check, arg = line_checking(line)
        if check:
            good_sort(line)
        else:
            bad_sort(line, arg)