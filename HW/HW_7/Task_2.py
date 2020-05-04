"""
# HW7 - Task № 2
Implement a project for calculating the total consumption of fabric for clothing production.
The main essence (class) of this project is clothing, which may have a specific name.
The types of clothing in this project include a coat and a suit. These types of clothes have
parameters: size (for a coat) and height (for a suit). These can be ordinary numbers: V and H, respectively.
To determine the fabric consumption for each type of clothing, use the formulas: for a coat (V / 6.5 + 0.5),
for a suit (2 * H + 0.3). Check the operation of these methods on real data. Implement a general calculation
of tissue consumption. Test in practice the knowledge gained in this lesson: implement abstract classes for
the main classes of the project, test in practice the work of the @property decorator.
"""
from abc import ABC, abstractmethod


class ClothesAbstract(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def add_coat(self, v) -> float:
        pass

    @abstractmethod
    def add_costume(self, h) -> float:
        pass

    @abstractmethod
    def sum_cloth_costs(self) -> float:
        pass


class Clothes(ClothesAbstract):

    def __init__(self, name):
        self.__name = name
        self.w = []
        self.result_costs = 0

    def add_coat(self, v):
        self.w.append(Coat(v))

    def add_costume(self, h):
        self.w.append(Costume(h))

    def sum_cloth_costs(self):
        self.result_costs = 0
        for itm in self.w:
            self.result_costs += itm.costs
        return self.result_costs

    @property
    def name(self):
        return self.__name


class Coat:
    def __init__(self, v):
        self.v = v
        try:
            self.costs = round(self.v / 6.5 + 0.5)
        except ValueError:
            print('Enter digit')
            self.costs = None


class Costume:
    def __init__(self, h):
        self.h = h
        try:
            self.costs = round(2 * self.h + 0.3)
        except ValueError:
            print('Enter digit')
            self.costs = None


project1 = Clothes('First project')
project1.add_coat(3)
project1.add_costume(7)
project1.add_coat(4)
project1.add_costume(3)
project1.sum_cloth_costs()

print(project1.name)
print(project1.sum_cloth_costs())
# print(project1.w)
print('\n')

project2 = Clothes('Second project')
project2.add_coat(32)
project2.add_costume(32)
project2.add_costume(23)
project2.sum_cloth_costs()

print(project2.name)
print(project2.sum_cloth_costs())
# print(project2.w)
print('\n')
