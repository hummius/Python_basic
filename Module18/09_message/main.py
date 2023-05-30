message = input('Сообщение: ').split()
words_list = []

for word in message:
    if word.isalpha():
        word = list(word[::-1])
        ''.join(word)
        words_list.extend(word)
        words_list.extend(' ')
    else:
        temp_letter = []
        temp_sym = []
        for index, sym in enumerate(list(word)):
            if sym.isalpha():
                temp_letter.append(sym)
            else:
                temp_sym.append([index, sym])
        temp_letter = list(temp_letter[::-1])
        for iteration in range(len(temp_sym)):
            temp_letter.insert(temp_sym[iteration][0], temp_sym[iteration][1])
        ''.join(temp_letter)
        words_list.extend(temp_letter)
        words_list.extend(' ')

print('\nНовое сообщение:', ''.join(words_list))
