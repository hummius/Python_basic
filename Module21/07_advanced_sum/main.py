def sum(*args):
    res = 0
    for elm in args:
        if isinstance(elm, int):
            res += elm
        if isinstance(elm, list):
            for sub_elm in elm:
                res += sum(sub_elm)
    return res
