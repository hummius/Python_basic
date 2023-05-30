amount = int(input('Введите количество пар слов: '))
words_dict = dict()

for iter in range(1, amount + 1):
    couple = input(f'{iter}-я пара: ').split(' - ')
    words_dict.update({couple[0].title(): couple[1].title()})
    words_dict.update({couple[1].title(): couple[0].title()})

while True:
    word = input('Введите слово: ').title()
    if word in words_dict:
        print(f'Синоним: {words_dict[word]}')
    else:
        print('Такого слова в словаре нет.')