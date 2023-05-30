players_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
day1_list = []

for index, i in enumerate(players_list):
    if (index) % 2 == 0:
        day1_list.append(i)

print('Первый день:', day1_list)
