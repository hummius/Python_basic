import random

sticks = int(input('Количество палок: '))
throws = int(input('Кол-во бросков: '))
sticks_stand = ['I' for _ in range(sticks)]

for i in range(throws):
    right_board = random.randint(3, sticks)
    left_board = random.randint(1, right_board)
    print('Бросок', str(i + 1) + '. Сбиты палки с номера', left_board, 'по номер', right_board)
    hit = ['.' for _ in range(right_board - left_board + 1)]
    sticks_stand[left_board - 1:right_board] = hit

print('\nРезультат:', ''.join(sticks_stand))