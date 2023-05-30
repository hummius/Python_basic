vowels = 'ауеыоэяиюёЁУЕЫАОЭЯИЮ'
text = input('Введите текст: ')

vowels_list = [letter for letter in text if letter in vowels]

print('\nСписок гласных букв:', vowels_list)
print('Длина списка:', len(vowels_list))