def sort(nums):
    swap = True
    while swap:
        swap = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swap = True

amount = int(input('Кол-во чисел в списке: '))
num_list = []

for _ in range(amount):
    number = int(input('Введите число: '))
    num_list.append(number)
print('Изначальный список:', num_list)

sort(num_list)
print('Отсорированный список:', num_list)
