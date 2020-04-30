"""
# HW6 - Task № 5
Implement the base class Car. This class should have the following
attributes: speed, color, name, is_police (boolean). As well as
methods: go, stop, turn (direction), which should report that the
car went, stopped, turned (where). Describe several child classes:
TownCar, SportCar, WorkCar, PoliceCar. Add the show_speed method to
the base class, which should show the current speed of the car. For
the TownCar and WorkCar classes, override the show_speed method. At
speeds above 60 (TownCar) and 40 (WorkCar), a speeding message should
be displayed.
"""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Start drawing with {self.title}')


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Start drawing with {self.title}')


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Start drawing with {self.title}')


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Start drawing with {self.title}')


itm = Stationery('nothing')
pen_itm = Pen('Pen')
p_itm = Pencil('Pencil')
h_itm = Handle('Handle')

itm.draw()
pen_itm.draw()
p_itm.draw()
h_itm.draw()
