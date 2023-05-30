friends_num = int(input('Кол-во друзей: '))
friends_list = []
for friend in range(friends_num):
    friends_list.append([friend + 1, 0])
debts_num = int(input('Долговых расписок: '))

for i in range(debts_num):
    print('\n' + str(i + 1) + '-я расписка')
    creditor = int(input('Кому: '))
    debtor = int(input('От кого: '))
    size = int(input('Сколько: '))
    friends_list[creditor - 1][1] -= size
    friends_list[debtor - 1][1] += size

print('\nБаланс друзей')
for position in range(friends_num):
    print(str(friends_list[position][0]) + ':', friends_list[position][1])
