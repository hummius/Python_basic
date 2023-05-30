class Mydict(dict):
    """
    Класс Мой Словарь имитирующий работу словаря
    """
    def get(self, key) -> int:
        """
        Функция совершающая поиск ключа и выводящая его значение

        :param key: ключ для поиска в словаре

        :return: Значение, если есть ключ. Иначе: 0
        """
        return super().get(key, 0)


my_dict = Mydict({'a': 1, 'b': 2})

print(my_dict.get('a'))
print(my_dict.get('b'))
print(my_dict.get('c'))
