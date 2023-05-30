numbers_amount = int(input('Кол-во чисел: '))
numbers_list = []
add_list = []
count = 0
temp = 0

for i in range(numbers_amount):
    number = int(input('Число: '))
    numbers_list.append(number)
print('\nПоследовательность:', numbers_list)

for i in range(numbers_amount - 1, -1, -1):
    if numbers_list[numbers_amount - 1] != numbers_list[i]:
        temp = i
        break
for y in range(temp, -1, -1):
    count += 1
    add_list.append(numbers_list[y])
print('Нужно приписать чисел:', count)
print('Сами числа:', add_list)