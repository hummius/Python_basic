word = input('Введите слово: ')
word_list = list(word)
amount = len(word_list)
count = -1
mirror_list = []

for i in range(amount):
    mirror_list.append(word_list[count])
    count -= 1

if ''.join(mirror_list) == word:
    print('\nСлово является палидромом')
else:
    print('\nСлово не является полидромом')