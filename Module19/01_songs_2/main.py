violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

amount = int(input('Сколько песен выбрать? '))
total_time = 0

for num in range(1, amount + 1):
    title = input(f'Название {num} песни: ')
    if title in violator_songs:
        total_time += violator_songs[title]
    else:
        print('Ошибка: такой песни нет в списке')

print('\nОбщее время звучания песен:', round(total_time, 2))