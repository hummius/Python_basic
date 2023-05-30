import itertools


pin = (3, 6, 3, 7)


numbers = range(10)

pincode_vars = itertools.product(numbers, repeat=4)

for var in pincode_vars:
    if var == pin:
        print(var)