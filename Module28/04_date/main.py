class Date:
    """
    Абстрактный класс Дата
    """
    @classmethod
    def from_string(cls, string: str) -> str:
        """
        Функция возвращающая строку с датой

        :param string: вводная строка
        :return: str
        """
        date_list = string.split('-')
        return f'День: {date_list[0]}       ' \
               f'Месяц: {date_list[1]}       ' \
               f'Год: {date_list[2]}'

    @classmethod
    def is_date_valid(cls, string: str) -> bool:
        """
        Функция проверяющая корректность даты

        :param string: вводная строка
        :return: True или False
        """
        day, month, year = string.split('-')
        if 0 < int(day) < 32 and 0 < int(month) < 13:
            return True
        else:
            return False

date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))