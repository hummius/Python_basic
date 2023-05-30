string = input('Введите строку: ').split()
longest = ''

for i in range(len(string)):
    if len(string[i]) > len(longest):
        longest = string[i]

print('Самое длинное слово:', longest)
print('Длина этого слова:', len(longest))