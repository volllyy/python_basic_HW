from random import choice


class Wolf:

    def __init__(self, w_type):
        self.w_type = w_type

    def ask(self):
        print('UUUUUUUUUUURRRRRRR')

    def run(self):
        for idx in range(10):
            print(idx)

    def reproduction(self, other):
        return Wolf(choice((self.w_type, other.w_type)))


class Homo:
    __population = []

    def __init__(self, eye_color):
        self.age = 0
        self.sex = choice(('m', 'f'))
        self.eye_color = eye_color
        Homo.__population.append(self)

    def get_population(self):
        return tuple(self.__population)

    def ask(self):
        print('dasdasda')

    def reproduction(self, other):
        cls = type(self)
        return cls(choice((self.eye_color, other.eye_color)))


class HomoSapience(Homo):

    def __init__(self, name, *args, **kwargs):
        self.name = name
        super().__init__(*args, **kwargs)

    def ask(self):
        return f'My name is {self.name}'

    def reproduction(self, other):
        cls = type(self)
        return cls(name=other.name, eye_color=self.eye_color)


class WereWolf(HomoSapience, Wolf):
    def __init__(self, name, w_type, *args, **kwargs):
        super().__init__(name, *args, **kwargs)
        Wolf.__init__(self, w_type)

    def __moon(self):
        return choice((1, 2, 3, 4))

    def ask(self):
        moon = self.__moon()

        if moon & 1:
            print(f"Who am I?")
        elif not moon & 1:
            print('RRRRRRRRRRRRR')

    def reproduction(self, other):
        cls = type(self)
        return cls(name=other.name, eye_color=choice((self.eye_color, other.eye_color)), w_type=self.w_type)


homo1 = Homo(eye_color='RED')
homo2 = Homo(eye_color='GREEN')
homsap1 = HomoSapience('Vasya', 'Blue')
ww1 = WereWolf('Joe', 'ALPHA', 'Brown')
print(1)
