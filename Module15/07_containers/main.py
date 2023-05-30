containers_amount = int(input('Количество контейнеров: '))
containers_list = []

for _ in range(containers_amount):
    weight = int(input('Введите вес контейнера: '))
    containers_list.append(weight)

new_container = int(input('\nВведите вес нового контейнера: '))

for index, i in enumerate(containers_list):
    if i <= new_container:
        print('\nНомер, который получит новый контейнер:', index + 1)
        break