num_list = []
new_list = []

for _ in range(5):
    number = int(input('Введите число: '))
    num_list.append(number)

shift = int(input('Сдвиг: '))
count = 0

for _ in range(5):
    new_list.append(num_list[shift * -1 + count])
    count += 1

print('Изначальный список', num_list)
print('Сдвинутый список:', new_list)

