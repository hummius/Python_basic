def num_reverse(x):
    whole_num = int(x)
    fractional = (x - int(x)) * 100
    res_1 = 0
    res_2 = 0
    while whole_num != 0:
        res_1 *= 10
        res_1 += whole_num % 10
        whole_num //= 10
    while fractional != 0:
        res_2 *= 10
        res_2 += fractional % 10
        fractional //= 10
    result = res_1 + (res_2 / 100)
    return result
num_1 = float(input('Введите первое число: '))
num_2 = float(input('Введите второе число: '))

rev_1 = num_reverse(num_1)
rev_2 = num_reverse(num_2)

print('\nПервое число наоборот:', round(rev_1, 2))
print('Второе число наоборот:', rev_2)
print('Сумма:', round(rev_1 + rev_2, 2))
