cards_amount = int(input('Количество видеокарт: '))
cards_list = []
new_cars_list = []

for i in range(cards_amount):
    print(i + 1, 'Видеокарта:', end = ' ')
    videocard = int(input())
    cards_list.append(videocard)

for i in cards_list:
    if i < max(cards_list):
        new_cars_list.append(i)

print('Старый список видеокарт:', cards_list)
print('Новый список видеокарт', new_cars_list)
