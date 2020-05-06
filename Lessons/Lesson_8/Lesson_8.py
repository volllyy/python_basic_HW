import requests


class MyError(Exception):
    def __init__(self, text=''):
        self.text = text


class Product:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return getattr(self, 'name')


class SpecialOfferCatalog:
    headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

    def __init__(self, url: str):
        self.__url = url
        self.__products = []

    def __parse__(self):
        url = self.__url
        while url:
            response = requests.get(url, headers=self.headers)
            data = response.json()
            url = data['next']
            self.__products.extend([Product(**itm) for itm in data['results']])


class MyMath:
    __population = 222

    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def division(a, b):
        return a / b

    @classmethod
    def some(cls):
        return cls.__population


if __name__ == '__main__':
    url = 'https://5ka.ru/api/v2/special_offers/'
    catalog = SpecialOfferCatalog(url)
    print(1)

