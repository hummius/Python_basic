import random

length = int(input('Введите длину списка: '))

num_list = [random.randint(1, 100) for _ in range(length)]
num_list = [1 if index % 2 == 0 else num_list[index] % 5 for index in range(len(num_list))]

print('Результат:', num_list)