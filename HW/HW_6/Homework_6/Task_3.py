"""
# HW6 - Task № 3
Implement the base class Worker, in which the attributes are defined:
name, surname, position (position), income (income). The last attribute
must be protected and refer to a dictionary containing elements: salary
and bonus, for example, {"wage": wage, "bonus": bonus}. Create the Position
class based on the Worker class. In the Position class, implement methods
for obtaining the full name of the employee (get_full_name) and income,
taking into account the premium (get_total_income). Check the operation of
the example on real data (create instances of the Position class, transfer
data, check attribute values, call instance methods).
"""


class Worker:

    def __init__(self,  name, surname, position, __income, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': int(wage), 'bonus': int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, __income, wage, bonus):
        super().__init__(name, surname, position, __income, wage, bonus)

    def get_full_name(self):
        return print(f'Full name: {self.name} {self.surname}')

    def get_total_income(self):
        try:
            return print(f'Full income: {sum(self.bonus, self.wage)}')
        except ValueError:
            return print('Enter correct data')


pos = Position('Vova', 'Antonenko', 'manager', {'wage': 10, 'bonus': 9}, 10,  9)
pos1 = Position('Dima', 'Andreev', 'manager', {'wage': 14, 'bonus': 32}, 14,  32)
pos.get_full_name()
pos.get_total_income()
pos1.get_full_name()
pos1.get_total_income()
