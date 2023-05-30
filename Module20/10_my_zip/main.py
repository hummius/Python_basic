string = input('Строка: ')
string = list(string)
tpl_numbers = tuple(i * 10 for i in range(1, len(string) + 1))
print(f'Кортеж чисел: {tpl_numbers}')

print('\nРезультат: ')
gen_tpl = ((string[i], tpl_numbers[i]) for i in range(len(string)))
print(gen_tpl)
for element in tuple(gen_tpl):
    print(element)
