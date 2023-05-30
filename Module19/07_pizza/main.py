orders_amount = int(input('Введите кол-во заказов: '))
clients_dict = dict()

for num in range(1, orders_amount + 1):
    order = input(f'{num} заказ: ').split()
    if not order[0] in clients_dict:
        clients_dict.update({order[0]: {order[1]: int(order[2])}})
    else:
        if not order[1] in clients_dict[order[0]]:
            clients_dict[order[0]].update({order[1]: int(order[2])})
        else:
            clients_dict[order[0]][order[1]] += int(order[2])

for client in clients_dict:
    print(f'{client}:')
    for pizza in clients_dict[client]:
        print(f'        {pizza}: {clients_dict[client][pizza]}')