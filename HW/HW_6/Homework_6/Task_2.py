"""
# HW6 - Task № 2
Implement the Road class, in which the attributes are defined:
length (length), width (width). The values ​​of these attributes
must be passed when the class is instantiated. Attributes to
make protected. Determine the method for calculating the mass
of asphalt required to cover the entire roadway. Use the formula:
the length, the width and the mass of the asphalt to cover one square meter of the
road with asphalt, 1 cm thick * the number of cm of the thickness of
the canvas. Check the method.
"""


class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculation(self):
        mass = 25
        thick = 5
        try:
            result = self.__length * self.__width * mass * thick
            print(f'{self.__length}m * {self.__width}m * {mass}kg * {thick}cm = {result // 1000}T')
        except TypeError:
            print(f'Enter correct data for {self}')


road = Road(length='a', width=5000)
road1 = Road(length=12, width=435)
road.calculation()
road1.calculation()
