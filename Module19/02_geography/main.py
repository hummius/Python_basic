amount = int(input('Кол-во стран: '))
country_dict = dict()

for num in range(1, amount + 1):
    country = input(f'{num} страна: ').split()
    country_dict.update({country[0] : country[1:]})

for num in range(1, 4):
    city = input(f'\n{num} город: ')
    check = False
    for cntry in country_dict:
        if city in country_dict[cntry]:
            print(f'Город {city} расположен в стране {cntry}')
            check = True
    if not check:
        print(f'По городу {city} данных нет.')