import os

def cesar_cipher():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher_text = []
    file = open(os.path.abspath('text.txt'), 'r')
    for index, line in enumerate(file.readlines()):
        for letter in line:
            if letter.lower() in list(alphabet):
                for i, alp_let in enumerate(list(alphabet)):
                    if letter.lower() == alp_let:
                        if i + (index + 1) > len(list(alphabet)) - 1:
                            if not letter.isupper():
                                cipher_text.extend(list(alphabet[i + (index + 1) - 26]))
                            else:
                                cipher_text.extend(list(alphabet[i + (index + 1) - 26].upper()))
                        else:
                            if not letter.isupper():
                                cipher_text.extend(list(alphabet[i + (index + 1)]))
                            else:
                                cipher_text.extend(list(alphabet[i + (index + 1)].upper()))

            else:
                cipher_text.extend(letter)
    file.close()
    file_cipher = open(os.path.abspath('cipher_text.txt'), 'w+')
    file_cipher.write(''.join(cipher_text))

file_text = open(os.path.abspath('text.txt'), 'w+')
text = input('Введите текст для файла (через пробел): ').split()
text = '\n'.join(text)
file_text.write(text)
file_text.close()

cesar_cipher()