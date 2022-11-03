import json


class Converter:
    def __init__(self, json):
        for key, value in json.items():
            self.__setattr__(key, value)

    def __str__(self):
        return str(self.__dict__)


class ColorizeMixin:

    def __repr__(self, repr_color_code):
        return f'\033[1;{repr_color_code};40m'


class Advert(ColorizeMixin):
    repr_color_code = 33

    def __init__(self, json):
        for key, value in json.items():
            self.__setattr__(key, value)

    def __setattr__(self, key, value):
        if key == 'price' and value < 0:
            raise ValueError('price must be >= 0')
        if key == 'location':
            value = Converter(value)
        super().__setattr__(key, value)

    def __getattribute__(self, item):
        if item == 'price' and item not in self.__dict__:
            return 0
        return super().__getattribute__(item)

        def __repr__(self):
        return super().__repr__(Advert.repr_color_code)\
               + f'{self.title} | {self.price}₽'
