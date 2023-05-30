def coin_search(x, y, r):
    if (x ** 2 + y ** 2) <= r:
        print('\nМонетка где-то рядом')
    else:
        print('\nМонетки в области нет')

print('Введите координаты монетки:')
num_x = float(input('X: '))
num_y = float(input('Y: '))
radius = int(input('Введите радиус: '))

coin_search(num_x, num_y, radius)