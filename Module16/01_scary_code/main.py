main_list = [1, 5, 3]
first_list = [1, 5, 1, 5]
second_list = [1, 3, 1, 5, 3, 3]

main_list.extend(first_list)
print('Количество цифр 5 при первом объединении:', main_list.count(5))
for i in range(main_list.count(5)):
    main_list.remove(5)

main_list.extend(second_list)
print('Количество цифр 3 при втором объединении:', main_list.count(3))

print('Итоговый список:', main_list)