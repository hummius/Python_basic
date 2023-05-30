import os

zen_file = open(os.path.join('zen.txt'), 'r')
for line in zen_file.readlines()[::-1]:
    print(line, end='')
zen_file.close()