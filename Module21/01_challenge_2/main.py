def num_count(num):
    if num == 0:
        return
    num_count(num - 1)
    print(num)

number = int(input('Введите num: '))

num_count(number)