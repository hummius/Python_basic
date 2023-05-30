ip_address = input('Введите IP: ').split('.')
correct = True

if len(ip_address) == 4:
    for index in ip_address:
        if not index.isdigit():
            print(index, '- это не целое число.')
            correct = False
        elif int(index) > 255:
            print(index, 'превышает 255.')
            correct = False
        elif int(index) < 0:
            print(index, 'меньше 0.')
            correct = False
else:
    print('Адрес — это четыре числа, разделённые точками.')
    correct = False

if correct:
    print('IP-адрес корректен.')