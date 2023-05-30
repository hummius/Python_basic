number = int(input('Введите число: '))
num_list = []

for i in range(1, number):
    if i % 2 != 0:
        num_list.append(i)

print('\nСписок нечётных чисел от одного до N:', num_list)