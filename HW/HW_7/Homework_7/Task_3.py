"""
# HW7 - Task № 3
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное
(не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения до
целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида **\n\n***..., где количество
ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются
все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: **\n\n. Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: **\n\n***.
"""


class Cell:

    def __init__(self, cells: float):
        self.__cells = cells

    def __add__(self, other):
        return Cell(self.__cells + other.cells)

    def __sub__(self, other):
        if self.__cells >= other.cells:
            return Cell(self.__cells - other.cells)
        else:
            print('Cant sub\n')
            return None

    def __mul__(self, other):
        return Cell(self.__cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.__cells // other.cells)

    def make_order(self, n: int):
        x = self.__cells / n
        y = self.__cells // n
        str1 = '*'
        if x > y:
            for i in range(int(y)):
                print(n * str1)
            print((int(self.__cells - (y * n)) * str1) + '\n')
        else:
            for i in range(int(y)):
                print((n * str1))

    @property
    def cells(self):
        return self.__cells


cell1 = Cell(10)                            # examples of all methods with cell1 and cell2
cell2 = Cell(5)
cell3 = cell1 + cell2
cell4 = cell1 - cell2
cell5 = cell1 * cell2
cell6 = cell1 / cell2

print(cell3.cells)                          # conclusions of operations with cell1 and cell2
print(cell4.cells)
print(cell5.cells)
print(cell6.cells)

cell3.make_order(4)                         # example of method make_order with 4 '*' in 3 lines and 2 '*' in last line
cell3.make_order(4)                         # example of method make_order with 5 '*' in 3 lines
cell5.make_order(22)                        # example of method make_order with 22 '*' in 2 lines and 6 '*' in last line

cell7 = cell2 - cell1                       # example of impossible subtraction

cell8 = cell3 / cell6                       # example of integer division
print(cell8.cells)

cell9 = Cell('d')                           # examples of wrong attributes for class Cell
cell10 = Cell('1')
