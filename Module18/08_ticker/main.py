first_str = input('Первая строка: ')
second_str = input('Вторая строка: ')
second_str = list(second_str)
impossible = True

for i in range(len(second_str)):
    second_str = second_str[1:] + second_str[:1]
    if second_str == list(first_str):
        print('\nПервая строка получается из второй со сдвигом', i + 1)
        impossible = False

if impossible:
    print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')