def tpl_sort(tpl):
    integer = True
    for num in tpl:
        if abs(num) % int(abs(num)) > 0:
            integer = False
    if integer:
        tpl = tuple(sorted(list(tpl)))
    return tpl