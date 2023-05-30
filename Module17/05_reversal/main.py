string = input('Введите строку: ')

indexes = [i for i in range(len(string)) if string[i] == 'h']

print('Развернутая последовательность между первым и последним h:', string[max(indexes) - 1:min(indexes):-1])