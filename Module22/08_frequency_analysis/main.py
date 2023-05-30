import os

def frequency_analysis():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(alphabet)
    letters_amount = 0
    letters_dict = dict()

    file_in = open(os.path.abspath('text.txt'), 'r')
    for symbol in file_in.read():
        if symbol.lower() in alphabet:
            letters_amount += 1
            if not symbol.lower() in letters_dict:
                letters_dict.update({symbol.lower(): 1})
            else:
                letters_dict[symbol.lower()] += 1

    file_out = open(os.path.abspath('analysis.txt'), 'w+')
    result_dict = {key: round(value / letters_amount, 3) for val in sorted(letters_dict.values(), reverse=True)
                   for key, value in sorted(letters_dict.items()) if value == val}
    for key, value in result_dict.items():
        file_out.write(f'{key} {value}\n')
    file_out.close()



frequency_analysis()