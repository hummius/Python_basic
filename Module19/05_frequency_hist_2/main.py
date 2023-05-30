def inverted_dict(dictionary):
    new_dict = dict()
    maximum = max(dictionary.values())
    for iter in range(1, maximum + 1):
        new_dict.update({iter: []})
        for symbol in dictionary:
            if dictionary[symbol] == iter:
                new_dict[iter].append(symbol)
    return new_dict

text = input('Введите текст: ')
text_list = list(text)
dictionary = dict()

for sym in text_list:
    amount = text.count(sym)
    dictionary.update({sym: amount})

print('Оригинальный словарь частот:')
for i in sorted(dictionary):
    print(f'{i} : {dictionary[i]}')

print('\nИнвертированный словарь частот:')
result = inverted_dict(dictionary)
for view in result:
    print(f'{view} : {result[view]}')