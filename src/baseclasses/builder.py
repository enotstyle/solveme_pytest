

class BuilderBaseClass:
    """
    Базовый класс для билдера.
    """
    def __init__(self):
        self.result = {}

    def update_inner_value(self, keys, value):
        """
        Метод добавляет/обновляет значение в объекте на
        указанном уровне.
        """
        if not isinstance(keys, list):
            self.result[keys] = value
        else:
            temp = self.result
            for item in keys[:-1]:
                if item not in temp.keys():
                    temp[item] = {}
                temp = temp[item]
            temp[keys[-1]] = value
        return self

    def build(self):
        return self.result
