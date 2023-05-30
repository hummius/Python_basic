import random

original_list = [random.randint(0, 9) for _ in range(10)]
print(f'Оригинальный список: {original_list}')
new_list = list()
temp_list = list()

for index, number in enumerate(original_list):
    if (index + 1) % 2 != 0:
        temp_list.append(number)
    else:
        temp_list.append(number)
        new_list.append(tuple(temp_list))
        temp_list = []

print(f'Новый список по первому способу: {new_list}')

new_list = []
for i in range(0, 10, 2):
    element = (original_list[0 + i], original_list[1 + i])
    new_list.append(element)

print(f'Новый список по второму способу: {new_list}')

new_list = []
for _ in range(5):
    element = (original_list.pop(0), original_list.pop(0))
    new_list.append(element)
print(f'Новый список по третьему способу: {new_list}')