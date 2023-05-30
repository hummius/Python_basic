alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
ciphertext = []

for y in list(text):
    if y in list(alphabet):
        for index, i in enumerate(list(alphabet)):
            if y == i:
                if index + shift > len(list(alphabet)) - 1:
                    ciphertext.extend(list(alphabet[index + shift - 33]))
                else: ciphertext.extend(list(alphabet[index + shift]))
    else:
        ciphertext.extend(y)

print('Зашифрованное сообщение:', ''.join(ciphertext))