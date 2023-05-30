site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

def site_maker(struct, **kwargs):
    for key, value in kwargs.items():
        if key in struct:
            struct[key] = value

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            site_maker(sub_struct, **kwargs)
    return struct

amount = int(input('Сколько сайтов: '))
for i in range(amount):
    name = input('Введите название продукта для нового сайта: ')
    new_site = site_maker(site,
                          title=f'Куплю/продам {name} недорого',
                          h2=f'У нас самая низкая цена на {name}')
    print(f'Сайт для {name}: {new_site}')