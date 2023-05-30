string = input('Введите строку: ')
string = list(string)
string.append('')
encoded_str = []
prev_symbol = ''
count = 0

for symbol in string:
    if symbol == prev_symbol:
        count += 1
        prev_symbol = symbol
    else:
        encoded_str.append(f'{prev_symbol}{count}')
        count = 1
        prev_symbol = symbol

print('Закодированная строка:', ''.join(encoded_str[1:]))