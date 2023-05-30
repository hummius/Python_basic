import os
from _collections_abc import Iterable


def gen_files_path(to_find: str, directory='C:\\') -> Iterable[str]:
    """
    Функция-генератор для поиска каталога и вывода пути ко всем файлам каталога

    :param to_find: имя каталога для поиска
    :param directory: директория для поиска (по умолчанию C:\\)
    :return:
    """
    for link, dirs, files in os.walk(directory):
        if link.split("\\")[-1] == to_find:
            for file in files:
                yield os.path.join(link, file)
            return


name_of_catalog = input('Введите имя каталога для поиска: ')
paths_list = []
for files_paths in gen_files_path(name_of_catalog):
    print(files_paths)
