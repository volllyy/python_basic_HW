"""
# HW6 - Task № 4
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
import random


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed:
            print(f'{self.name} car is going')
        else:
            print(f'{self.name} has 0 speed')

    def stop(self):
        if not self.speed:
            print(f'{self.name} car stopped')
        else:
            print(f'{self.name} has not 0 speed')

    def turn(self):
        print(f'{self.name} car turned {random.choice(("left", "right"))}')

    def show_speed(self):
        try:
            float(self.speed)
            print(f'{self.name} speed is {self.speed} km/h')
        except ValueError:
            print(f'{self.name} speed should be a digit')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        try:
            if self.speed > 60:
                print(f'{self.name} speed is {self.speed} km/h Over speed!!!')
            else:
                print(f'{self.name} speed is {self.speed} km/h')
        except TypeError:
            print(f'{self.name} speed should be a digit')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        try:
            if self.speed > 40:
                print(f'{self.name} speed is {self.speed} km/h Over speed!!!')
            else:
                print(f'{self.name} speed is {self.speed} km/h')
        except TypeError:
            print(f'{self.name} speed should be a digit')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


car = Car(100, 'RED', 'Hyundai')
car1 = Car(50, 'WHITE', 'Smart')
car2 = Car('a', 'a', 'a')
t_car = TownCar(34, 'BLACK', 'Peugeot')
t_car1 = TownCar(120, 'YELLOW', 'Toyota')
t_car2 = Car('a', 'a', 'a')
w_car = WorkCar(25, 'BLACK', 'Opel')
w_car1 = WorkCar(76, 'ORANGE', 'Renault')
w_car2 = Car('a', 'a', 'a')
s_car = SportCar(300, 'RED', 'Ferrari')
p_car = PoliceCar(100, 'WHITE', 'Mercedes-Benz')

car.show_speed()
car1.show_speed()
car2.show_speed()
t_car.show_speed()
t_car1.show_speed()
t_car2.show_speed()
w_car.show_speed()
w_car1.show_speed()
w_car2.show_speed()
s_car.show_speed()
p_car.show_speed()
print(p_car.is_police, s_car.color, t_car.name)
print(w_car.color, t_car1.speed, car1.name)
s_car.go()
s_car.turn()
