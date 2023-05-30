string = input('Введите строку: ')
letter_set = set()
alone_list = list()
letter_list = list()

for i in list(string):
    if list(string).count(i) > 1:
        letter_set.add(i)
        letter_list = sorted(list(letter_set))
    else:
        alone_list.append(i)
frst_part = ''.join(letter_list)
letter_list.extend(alone_list)
scnd_part = ''.join(reversed(letter_list))
result = frst_part + scnd_part

if result == ''.join(reversed(result)):
    print('Можно сделать палидромом')
else:
    print('Нельзя сделать полидромом')