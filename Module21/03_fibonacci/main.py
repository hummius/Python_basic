def fibonachi(num_pos):
    if num_pos in (1, 2):
        return 1
    return fibonachi(num_pos - 1) + fibonachi(num_pos - 2)

num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
print(f'Число: {fibonachi(num_pos)}')