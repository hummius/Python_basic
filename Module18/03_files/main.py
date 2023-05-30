file_name = input('Название файла: ')
forbidden_list = ['@', '№', '$', '%', '^', '&', '/', '*', '(', ')']
appropriate = True

for sym in forbidden_list:
    if file_name.startswith(sym):
        print('\nОшибка: название начинается на один из специальных символов.')
        appropriate = False
        break
if not file_name.endswith('.txt') and not file_name.endswith('.docx'):
    print('\nОшибка: неверное расширение файла. Ожидалось .txt или .docx')
    appropriate = False

if appropriate:
    print('\nФайл назван верно.')