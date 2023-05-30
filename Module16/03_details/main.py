shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

ditail_name = input('Название детали: ')
amount = 0
total_price = 0

for i in shop:
    if i[0] == ditail_name:
        amount += 1
        total_price += i[1]
print('Кол-во деталей -', amount)
print('Общая стоимость -', total_price)
