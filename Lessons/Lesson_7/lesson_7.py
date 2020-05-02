import time
from abc import ABC, abstractmethod
from random import choice


class CarAbstract(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def turn_on(self, key) -> bool:
        pass

    @abstractmethod
    def turn_off(self) -> bool:
        pass


class Car(CarAbstract):

    def __init__(self, name, brand):
        self.__name = name
        self.brand = brand

    def turn_on(self, key) -> bool:
        if key:
            return True
        return False

    def turn_off(self) -> bool:
        return True

    @property
    def name(self):
        return self.__name


my_car = Car('Mustang', 'Ford')
print(1)


class Human:

    def __init__(self, name, surname, sex):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.__start_age = time.time()

    @property
    def age(self):
        return (time.time() - self.__start_age) // 10

    @property
    def start_age(self):
        return self.__start_age

    @start_age.setter
    def start_age(self, data):
        print('yo', data)

    def __add__(self, other):
        if self.sex == other.sex:
            return None
        return Human(other.name, self.surname, choice(('m', 'f')))

    def __str__(self):
        return f'{self.name} - {self.surname} - {self.age}'


class HomeIterator:

    def __init__(self, population: tuple):
        self.i = len(population) - 1
        self.__population = population

    def __next__(self):
        while True:
            if self.i < 0:
                raise StopIteration
            if self.__population[self.i].sex == 'm':
                self.i -= 1
            else:
                result = self.__population[self.i]
                self.i -= 1
                return result






class Home:

    def __init__(self, address):
        self.address = address
        self.__people = []

    def insert(self, human: Human):
        self.__people.append(human)

    def __call__(self, human: Human):
        self.insert(human)

    def __iter__(self):
        return HomeIterator(tuple(self.__people))


home = Home('sdsaafaf')
vasya = Human('vasya', 'ivanov', 'm')
petya = Human('petya', 'petrov', 'm')
masha = Human('masha', 'sidorova', 'f')

child = vasya + petya
child1 = vasya + masha

_ = [home(human) for human in (vasya, petya, masha, child1)]

print(1)

for human in home:
    print(human)

print(1)
#
#
# def mydeco(funk):
#     def wrap(*args, **kwargs):
#         print('START DECO WRAP')
#         print(funk.__name__)
#         tmp = funk(*args, **kwargs)
#         print('END DECO')
#         return tmp
#
#     return wrap
#
#
# # @mydeco
# def task1(x, y):
#     return x ** y
#
#
# @mydeco
# def task2():
#     print('Hello')
#
#
# test1 = task1(2, 4)
# print(test1)
# # test2 = task2()
