num_people = int(input('Кол-во человек: '))
people_list = list(range(1, num_people + 1))
number = int(input('Какое число в считалке? '))
print('Значит выбывает каждый', str(number) + '-й человек')
count = 0

for _ in range(num_people - 1):
    print('\nТекущий круг людей:', people_list)
    start = count % len(people_list)
    count = (start + number - 1) % len(people_list)
    print('Начало счёта номера', people_list[start])
    print('Выбывает человек под номером', people_list[count])
    people_list.remove(people_list[count])

print('\nОстался человек под номером', people_list[0])