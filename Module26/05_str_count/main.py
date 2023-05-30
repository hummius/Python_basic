import os
from _collections_abc import Iterable


def gen_count_py(directory: str) -> Iterable[int]:
    """
    Функция-генератор для поиска файлов с расширением .py и подсчета строк в этих файлах

    :param directory: путь к директории для поиска

    :return: int
    """
    for file in os.listdir(directory):
        count = 0
        if os.path.isfile(os.path.join(directory, file)):
            if file.endswith('.py'):
                print(file, end=' ')
                with open(os.path.join(directory, file), 'r', encoding='utf-8') as open_file:
                    for line in open_file.readlines():
                        if '#' not in line and len(line) > 1:
                            count += 1
                print(count)
            yield count


path = input('Введите путь к директории: ')
result = 0
for count_file in gen_count_py(path):
    result += count_file
print(f'Общее количество строк файлов .py в директории "{path}" : {result}')
