import os

def file_content():
    file = open(os.path.join('numbers.txt'), 'r')
    numbers_summ = 0

    print('Содержимое файла numbers.txt')
    for line in file.readlines():
        print(line)
        for elem in line:
            if elem.isdigit():
                numbers_summ += int(elem)
    file.close()
    return numbers_summ

answer_file = open(os.path.join('answer.txt'), 'w')
answer_file.write(str(file_content()))
answer_file.close()

answer_file = open(os.path.join('answer.txt'), 'r')
print('\nСодержимое файла answer.txt')
print(answer_file.read())
answer_file.close()