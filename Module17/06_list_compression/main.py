import random

amount = int(input('Количество чисел: '))
num_list = [random.randint(0, 2) for _ in range(amount)]
count = 0
print('Список до сжатия:', num_list)

for i in range(amount):
    index = i - count
    if num_list[index] == 0:
        num_list.append(num_list.pop(index))
        count += 1
result = [num_list.remove(0) for _ in range(count)]

print('Список после сжатия:', num_list)