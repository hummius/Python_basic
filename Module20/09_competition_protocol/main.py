records_amount = int(input('Сколько записей вносится в протокол? '))
records_dict = dict()

if records_amount < 3:
    print('Участников должно быть не меньше трех.')
else:
    for iter in range(1, records_amount + 1):
        value, key = input(f'{iter}-я запись: ').split()
        if int(value) > records_dict.get(key, 0):
            records_dict[key] = int(value)

    print('\nИтоги соревнований:')
    for i in range(3):
        max_key = ''
        max_num = 0
        for key, value in records_dict.items():
            if max_num < value:
                max_num = value
                max_key = key

        print('{place}-е место. {name} ({score})'.format(
                place=i, name=max_key, score=max_num))
        if records_dict.get(max_key, 0):
            records_dict.pop(max_key)