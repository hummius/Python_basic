people_amount = int(input('Введите количество человек: '))
tree_dict = dict()
count = 1
position = 0

while people_amount > 0:
    couple = input(f'{count}-я пара: ').split()
    count += 1
    if not couple[1] in tree_dict:
        tree_dict.update({couple[1]: position})
        position += 1
        tree_dict.update({couple[0]: position})
        position += 1
        people_amount -= 2
    else:
        if not couple[0] in tree_dict:
            tree_dict.update({couple[0]: tree_dict[couple[1]] + 1})
            people_amount -= 1
        else:
            print('Ошибка: данное имя уже подавалось.')

print('\n"Высота" каждого члена семьи:')
for member in sorted(tree_dict):
    print(member, tree_dict[member])