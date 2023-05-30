unique_list = [' ']

while True:
    word = input('Введите слово: ')
    unique_count = 0
    for i in list(word):
        equal = 0
        for letter in list(word):
            if letter == i:
                equal += 1
        if equal == 1:
            unique_list.append(i)
            unique_count += 1

    print('\nКол-во уникальных букв:', unique_count)