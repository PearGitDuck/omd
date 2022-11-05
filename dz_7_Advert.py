import json
import keyword


class Converter:
    def __init__(self, json):
        for key, value in json.items():
            if isinstance(value, dict):
                value = Converter(value)

            self.__setattr__(key, value)

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)


class ColorizeMixin:

    def __repr__(self):
        text_to_mod = super().__repr__()
        return f'\033[1;{self.repr_color_code};40m{text_to_mod}'


class BaseAdvert:
    repr_color_code = 33

    def __init__(self, json):

        for key, value in json.items():
            if keyword.iskeyword(key):
                key += '_'
            if isinstance(value, dict):
                value = Converter(value)
            self.__setattr__(key, value)

        if 'title' not in self.__dict__:
            raise ValueError('Нет атрибута title')

    @property
    def price(self):
        if '_price' not in self.__dict__:
            return 0
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError('price must be >= 0')
        else:
            self._price = new_price

    def __repr__(self):
        return f'{self.title} | {self.price}₽'


class Advert(ColorizeMixin, BaseAdvert):
    pass
