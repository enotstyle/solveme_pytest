from enum import Enum

class PyEnum(Enum):
    """
    Расширение Enum класса методом list, возвращающим список
    статусов, которые мы сможем использовать в нашем parametrize.
    """
    @classmethod
    def list(cls):
        print(cls)
        return list(map(lambda c: c.value, cls))
