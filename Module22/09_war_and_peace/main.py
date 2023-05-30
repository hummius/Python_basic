import os.path
import zipfile

def letters_statistic():
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet = list(alphabet)
    file_in = open(os.path.abspath('voyna-i-mir.txt'), 'r', encoding='utf-8')
    letters_dict = dict()
    total_amount = 0

    for line in file_in.readlines():
        for symbol in line:
            if symbol.lower() in alphabet:
                total_amount += 1
                if symbol in letters_dict:
                    letters_dict[symbol] += 1
                else:
                    letters_dict.update({symbol: 1})
    file_in.close()

    file_out = open(os.path.abspath('v&m_statistic.txt'), 'w+', encoding='utf-8')
    result_dict = {key: value for val in sorted(letters_dict.values(), reverse=True)
                   for key, value in sorted(letters_dict.items()) if value == val}

    for key, value in result_dict.items():
        file_out.write(f'** {key} ** кол-во в тексте: {value}\n'
                       f'        доля в тексте: {round(value / total_amount, 3)}\n\n')
    file_out.close()


zipFile = zipfile.ZipFile('voyna-i-mir.zip', 'r')
zipFile.extractall()
zipFile.close()

letters_statistic()