cells_amount = int(input('Количество клеток: '))
unusable_list = []

for i in range(1, cells_amount + 1):
    print('Эффективность', i, 'клетки:', end = ' ')
    efficiency = int(input())
    if efficiency < i:
        unusable_list.append(efficiency)

print('\nНеподходящие значения:', end = ' ')
for number in unusable_list:
    print(number, end = ' ')
