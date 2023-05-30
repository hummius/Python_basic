import random

maximum_number = int(input('Введите максимальное число: '))
hidden_num = random.randint(1, maximum_number)
result = set()

while True:
    numbers = input('\nНужное число есть среди вот этих чисел: ').split()
    if 'Помогите!' in numbers:
        print('Артём мог загадать следующие числа:', end=' ')
        for i in sorted(result):
            print(i, end=' ')
        break
    elif str(hidden_num) in numbers:
        print('Ответ Артёма: Да')
        if result == set():
            result = set(numbers)
        else:
            result = result & set(numbers)
    else:
        print('Ответ Артёма: Нет')
        result = result - set(numbers)