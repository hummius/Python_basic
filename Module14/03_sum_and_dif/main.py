def numbers_sum(x):
    sum = 0
    while x != 0:
        sum += x % 10
        x //= 10
    return sum

def numbers_amount(x):
    count = 0
    while x != 0:
        x //= 10
        count += 1
    return count

number = int(input('Введите число: '))

sum = numbers_sum(number)
amount = numbers_amount(number)

print('Сумма чисел:', sum)
print('Количествоцифр в числе:', amount)
print('Разность суммы и количества цифр:', abs(sum - amount))