func_dict = {}
def calculating_math_func(data, lst=func_dict):
    if data in lst:
        return (lst[data] / lst[data] ** 3) ** 10, 'из словаря'
    result = 1
    for index in range(2, data + 1):
        if index in lst:
            result = lst[index]
        else:
            result *= index
            lst.update({index: result})
    result /= result ** 3
    result = result ** 10
    return result

while True:
    number = int(input('Введите число: '))
    print(calculating_math_func(number))
    print(func_dict)
