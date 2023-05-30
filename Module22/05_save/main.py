import os

def file_saving(struct, path):
    if not os.path.exists(path):
        file = open(path, 'w+')
        file.write(struct)
        file.close()
        print('Файл успешно сохранён!')
    else:
        answer = input('Вы действительно хотите перезаписать файл? ').lower()
        if answer == 'да':
            file = open(path, 'w')
            file.write(text)
            file.close()
            print('Файл успешно перезаписан!')
        elif answer == 'нет':
            print('Введите путь: ')
            new_folder_sequence = input().split()
            new_file_name = input('\nВведите имя файла: ') + '.txt'
            new_path_to = os.path.join('C:/', '/'.join(new_folder_sequence), new_file_name)
            if os.path.exists(os.path.join('C:/', '/'.join(folder_sequence))):
                file_saving(text, new_path_to)
            else:
                print('Такого пути не существует.')
        else:
            print('Ошибка: такой команды не существует.')


text = input('Введите строку: ')
print('\nКуда хотите сохранить документ? Введите последовательность папок (через пробел):')
folder_sequence = input().split()

file_name = input('\nВведите имя файла: ') + '.txt'

path_to = os.path.join('C:/', '/'.join(folder_sequence), file_name)
if os.path.exists(os.path.join('C:/', '/'.join(folder_sequence))):
    file_saving(text, path_to)
else:
    print('Такого пути не существует.')