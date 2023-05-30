import random

first_list = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_list = [round(random.uniform(5, 10), 2) for _ in range(20)]

third_list = [first_list[i] if first_list[i] > second_list[i] else second_list[i] for i in range(20)]

print('Первая команда:', first_list)
print('Вторая команда:', second_list)
print('Победители тура:', third_list)