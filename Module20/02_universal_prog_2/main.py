def is_prime(data):
    data = list(data)
    prime_list = list()
    count = 0
    for index, symbol in enumerate(data):
        count = 0
        if index > 1:
            for i in range(2, index // 2 + 1):
                if index % i == 0:
                    count += 1
            if count <= 0:
                prime_list.append(symbol)
    return prime_list

print(is_prime('О Дивный Новый мир!'))
