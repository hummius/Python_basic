denied = True
digit_count = 0

while denied == True:
    password = input('Придумайте пароль: ')
    if len(password) >= 8:
        for i in list(password):
            if i.isupper():
                denied = False
            if i.isdigit():
                digit_count += 1
    if denied or digit_count < 3:
        print('Пароль ненадежный. Попробуйте еще раз.')
    else:
        print('Это надежный пароль!')
        break