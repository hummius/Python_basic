violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

amount = int(input('Сколько песен выбрать? '))
total_time = 0

for num in range(amount):
    failure = 0
    print('Название,', str(num + 1) + '-й песни:', end=' ')
    title = input()
    for song in violator_songs:
        if song[0] == title:
            total_time += song[1]

print('\nОбщее время звучания песен:', round(total_time, 2), 'минуты')