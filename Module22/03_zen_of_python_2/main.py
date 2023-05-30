import os

def letters_amount():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(alphabet)
    letters_count = dict()

    for letter in alphabet:
        count = 0
        file = open(os.path.join('..', '02_zen_of_python/zen.txt'), 'r')
        for elem in file.read():
            if elem.lower() == letter:
                count += 1
        if count > 0:
            letters_count.update({letter: count})
        file.close()

    return letters_count

def key_founder(dictionary):
    for key, value in dictionary.items():
        if value == min(dictionary.values()):
            return key

def words_amount():
    file = open(os.path.join('..', '02_zen_of_python/zen.txt'), 'r')
    count = 0
    file_work = file.readlines()

    for line in file_work:
        for word in line.split():
            count += 1
    file.close()
    return count - 1

def lines_amount():
    file = open(os.path.join('..', '02_zen_of_python/zen.txt'), 'r')
    result = len(file.readlines())
    file.close()
    return result

zen_file = open(os.path.join('..', '02_zen_of_python/zen.txt'), 'r')
letters_dict = letters_amount()

print(f'Кол-во букв в файле: {sum(letters_dict.values())}')
print(f'Кол-во слов в файле: {words_amount()}')
print(f'Кол-во строк в файле: {lines_amount()}')
print(f'Наиболее редкая буква: {key_founder(letters_dict)}')