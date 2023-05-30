def symbols_control(file):
    total_amount = 0

    for number, line in enumerate(file_orig.readlines()):
        if line.endswith('\n'):
            amount = len(line) - 1
        else:
            amount = len(line)
        total_amount += amount
        try:
            if amount < 3:
                raise ValueError(f'Ошибка: менее трёх символов в строке {number + 1}')
        except ValueError as exc:
            print(exc)
            with open('errors.log', 'a', encoding='utf-8') as errors_log:
                errors_log.write(f'{type(exc)} | {exc}\n')

    print(f'Общее количество символов: {total_amount}')

with open('people.txt', 'r', encoding='utf-8') as file_orig:
    symbols_control(file_orig)