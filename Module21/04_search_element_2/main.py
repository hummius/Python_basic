def key_search(struct, key, deep=None):
    if key in struct:
        return struct[key]

    for sub_struct in struct.values():
        if deep == 0:
            result = None
            break
        elif isinstance(sub_struct, dict):
            if deep != None:
                result = key_search(sub_struct, key, deep - 1)
            else:
                result = key_search(sub_struct, key)
            if result:
                break
    else:
        result = None

    return result

site = {
        'html': {
                'head': {
                        'title': 'Мой сайт'
                },
                'body': {
                        'h2': 'Здесь будет мой заголовок',
                        'div': 'Тут, наверное, какой-то блок',
                        'p': 'А вот здесь новый абзац'
                }
        }
}

key = input('Введите искомый ключ: ')
answer = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if answer == 'y':
    max_deep = int(input('Введите максимальную глубину: '))
    print('Значение ключа:', key_search(site, key, max_deep - 1))
elif answer == 'n':
    print('Значение ключа:', key_search(site, key))
else:
    print('Ошибка: не правильная команда.')