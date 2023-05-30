import os
def catalog_content(curr_path, lst):
    for elem in os.listdir(curr_path):
        path = os.path.join(curr_path, elem)
        if os.path.isfile(path):
            lst['files_amount'] += 1
            lst['catalog_size'] += os.path.getsize(path)
        if os.path.isdir(path):
            lst['catalog_amount'] += 1
            lst = catalog_content(path, lst)
    lst['catalog_size'] /= 1000
    return lst

user_path = input('Укажите путь: ')
lst_dict = {'catalog_amount' : 0, 'files_amount' : 0, 'catalog_size' : 0}

catalog_content(user_path, lst_dict)

print(f'Размер каталога (в Кб): {round(lst_dict["catalog_size"], 9)}'
      f'\nКоличество подкаталогов: {lst_dict["catalog_amount"]}'
      f'\nКоличество файлов: {lst_dict["files_amount"]}')