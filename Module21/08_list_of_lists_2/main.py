nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def list_rectifier(data):
    new_list = list()
    for elm in data:
        if isinstance(elm, int):
            new_list.append(elm)
        if isinstance(elm, list):
            new_list.extend(list_rectifier(elm))
    return new_list

print(list_rectifier(nice_list))

