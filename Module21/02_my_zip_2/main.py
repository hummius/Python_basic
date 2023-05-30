def my_zip(a, b, x):
    amount = [len(element) for element in (a, b, x)]
    res_list = [(tuple(a)[i], tuple(b)[i], tuple(x)[i]) for i in range(min(amount))]
    return res_list