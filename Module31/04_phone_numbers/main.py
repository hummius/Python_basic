import re


numbers_list = ['9999999999', '999999-999', '99999x9999']

for index, number in enumerate(numbers_list):
    if re.match(r'\b[8,9]\d{9}\b', number) == None:
        print(f'{index + 1} пример: не подходит')
    else:
        print(f'{index + 1} пример: все в порядке')
