def slicer(tpl, last_el):
    temp_list = list()
    count = 0
    for element in tpl:
        if element == last_el:
            count += 1
        if count >= 1:
            temp_list.append(element)
        if count >= 2:
            break
    return tuple(temp_list)