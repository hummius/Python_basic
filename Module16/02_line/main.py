first_line = list(range(160, 176 + 1, 2))
second_line = list(range(162, 180 + 1, 3))
first_line.extend(second_line)
main_line = []

for i in range(len(first_line)):
    main_line.append(min(first_line))
    first_line.remove(min(first_line))

print('Отсортированный список учеников:', main_line)