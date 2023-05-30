import time

def chat_menu():
    login = input('\nВведите свое имя: ')
    while True:
        try:
            choice = int(input('Посмотреть текущий текст чата (1)\n'
                               'Отправить сообщение (2)\n'
                               'Сменить имя (0)\n'))
            if choice == 1:
                chat_log_show(login)
            elif choice == 2:
                message_maker(login)
            elif choice == 0:
                login = input('\nСмена имени: ')
            else:
                raise Exception
        except (Exception, ValueError) as exc:
            print('\nОшибка: не правильно введена команда.\n')

def chat_log_show(key):
    with open('chat.log', 'r', encoding='utf-8') as log_file:
        for line in log_file.readlines():
            print(line)


def message_maker(key):
    message = input('Сообщение: ')
    with open('chat.log', 'a', encoding='utf-8') as message_file:
        message_file.write(f'|{time.asctime()}| *** {key} *** : {message}\n')


print("{:+^15}{:*^100}{:+^15}".format('', '@@ ДОБРО ПОЖАЛОВАТЬ В ЧАТ! @@', ''))
chat_menu()