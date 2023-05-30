import os

def second_tour_file():
    file_in = open(os.path.abspath('first_tour.txt'), 'r')
    passing_scr = ''
    scnd_tour_dict = dict()
    for index, line in enumerate(file_in.readlines()):
        if index == 0:
            for num in line:
                if num.isdigit():
                    passing_scr += num
        else:
            line = line.split()
            scnd_tour_dict.update({int(line[2]): line[0][0] + '. ' + line[1]})
    file_in.close()

    file_out = open(os.path.abspath('second_tour.txt'), 'w+')
    memb_count = 0
    file_out.write('   ')
    for key, value in sorted(scnd_tour_dict.items(), reverse=True):
        if key > int(passing_scr):
            memb_count += 1
            file_out.write(f'{str(memb_count)}) {value} {key}\n')
    file_out.seek(0)
    file_out.write(str(memb_count) + '\n')
    file_out.close()


file_first = open(os.path.abspath('first_tour.txt'), 'w+')
passing_score = input('Введите проходной бал: ')
file_first.write(passing_score + '\n')
members_amount = int(input('Кол-во участников: '))
for _ in range(members_amount):
    member = input('Введите имя участника и его балл: ')
    file_first.write(member + '\n')
file_first.close()

second_tour_file()