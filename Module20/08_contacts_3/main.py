def add_contact():
    full_name = input('Введите имя и фамилию нового контакта (через пробел): ').split()
    if tuple(full_name) in contact_dict:
        print('Такой человек уже есть в контактах.')
    else:
        phone_num = int(input('Введите номер телефона: '))
        contact_dict.update({tuple(full_name): phone_num})

def seach_contact():
    surname = input('Введите фамилию для поиска: ')
    for contact in contact_dict:
        if surname in contact or (surname + 'а') in contact:
            print(contact[0], contact[1], contact_dict[contact])

contact_dict = dict()

while True:
    print(f'Текщий словарь контактов: {contact_dict}')
    print('Введите номер действия:'
          '\n 1. Добавить Контакт'
          '\n 2. Найти человека')
    command = int(input(''))
    if command == 1:
       add_contact()
    elif command == 2:
        seach_contact()
    else:
        print('Ошибка: такой команды не существует.')