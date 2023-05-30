first_list = []
second_list = []

for i in range(3):
    print('Введите', str(i + 1) + '-e число для первого списка:', end=' ')
    number = int(input())
    first_list.append(number)

for i in range(7):
    print('Введите', str(i + 1) + '-e число для второго списка:', end=' ')
    number = int(input())
    second_list.append(number)

print('\nПервый список:', first_list)
print('\nВторой список:', second_list)
first_list.extend(second_list)

for i in first_list:
    amount = first_list.count(i)
    for interrations in range(amount):
        first_list.remove(i)
    first_list.insert(0, i)

print('\nНовый первый список с уникальными элементами:', first_list)