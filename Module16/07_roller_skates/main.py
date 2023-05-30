result = 0
skates_amount = int(input('Кол-во коньков: '))
skates_list = []
for i in range(skates_amount):
    print('Размер', str(i + 1) + '-й пары:', end=' ')
    pair_size = int(input())
    skates_list.append(pair_size)

num_people = int(input('\nКол-во людей: '))
foots_list = []
for person in range(num_people):
    print('Размер ноги', str(person + 1) + '-го человека:', end=' ')
    foot_size = int(input())
    for skates in skates_list:
        concurrence = False
        fits_list = []
        if foot_size <= skates:
            concurrence = True
            fits_list.append(skates)
        if concurrence:
            result += 1
            skates_list.remove(min(fits_list))

print('\nНаибольшее кол-во людей, которые могут взять ролики:', result)