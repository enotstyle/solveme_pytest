from faker import Faker

"""
Билдер для локализации.
"""


class PlayerLocalization:

    def __init__(self, lang):
        """
        Фейкер будет работать на том языке, который был передан в билдер.
        Объект будет наполнен также как другие подобные объекты, только
        на выбранном языке.
        """
        self.fake = Faker(lang)
        self.result = {
            'nickname': self.fake.first_name()
        }

    def set_number(self, number=11):
        """
        Добавляет в результат ключ number, со значение по умолчанию.
        """
        self.result['number'] = number
        return self

    def build(self):
        """
        Возвращает обьект в виде JSON.
        """
        return self.result
