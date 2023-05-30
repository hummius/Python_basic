def least_divisor(x):
    divisor = 2
    while True:
        if x % divisor == 0:
            result = divisor
            break
        else:
            divisor += 1
    return result

number = int(input('Введите число: '))

if number <= 1:
    print('Ошибка: число должно быть больше 1.')
else:
    result = least_divisor(number)
    print('Наименьший делитель, отличный от единицы:', result)