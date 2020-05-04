"""
# HW7 - Task № 1
Implement the Matrix class (matrix). Provide an overload of the class constructor (init () method),
which must receive data (list of lists) to form a matrix.
Hint: a matrix is ​​a system of some mathematical quantities arranged in the form of a rectangular diagram.
Examples of matrices you will find in the training manual.
The next step is to implement the overload of the str () method to display the matrix in its usual form.
Next, implement the overload of the add () method to implement the operation of adding two objects of the
Matrix class (two matrices). The result of the addition should be a new matrix.
Hint: the addition of matrix elements is done element by element - we add the first element of the first
row of the first matrix with the first element of the first row of the second matrix, etc.
"""
from copy import deepcopy as dc


class Matrix:

    def __init__(self, matrix: list):
        self.__matrix = matrix

    def __add__(self, other):
        f = True
        if len(self.__matrix) == len(other.__matrix):
            for el, itm in zip(self.__matrix, other.__matrix):
                if len(el) != len(itm):
                    print('Cannot perform the addition operation of matrices '
                          'of different sizes)\n')
                    f = False
        else:
            print('Cannot perform the addition operation of matrices '
                  'of different sizes\n')
            f = False

        if f:
            result = dc(self.__matrix)                                  # making a deepcopy of matrix
            j = 0
            for el, itm in zip(self.__matrix, other.__matrix):
                i = 0
                try:
                    for n, k in zip(el, itm):
                        result[j][i] = n + k
                        i += 1
                    j += 1
                except TypeError:
                    print(f'In one of the matrices 1) {self.__matrix} \n2) {other.__matrix} there are non-numeric '
                          f'elements, the addition operation is impossible\n')
                    f = False
            if f:
                return Matrix(result)

    def __str__(self):
        if self.__matrix:
            a = ''
            for itm in self.__matrix:
                a += '|'
                for j in itm:
                    a = a + "{: ^7d}".format(j)
                a += '| \n'
            return str(a)
        else:
            return None

        # return str('\n'.join(['  '.join([str(el) for el in itm])        A similar output of the matrix in one line,
        #                       for itm in self.__matrix])) + '\n'        but as for me through the format more clearly


matrix1 = Matrix([[1, 7, 5], [4, 5, 1], [5, 8, 7]])
matrix2 = Matrix([[5, 6, 1], [3, 3, 1], [3, 5, 6]])
matrix3 = matrix1 + matrix2

matrix4 = Matrix([[-153, 26, 56, 435, 2, -23], [47, -5, 100, 0, 24, 11]])
matrix5 = Matrix([[76, -2, 22, -333, 10, 3], [5, -55, 160, 78, 9, 56]])
matrix6 = matrix4 + matrix5

matrix11 = matrix3 + matrix1                                      # example of sum where 1 matrix is the sum of matrices

print(matrix1)
print(matrix3)
print(matrix5)
print(matrix6)
print(matrix11)

matrix8 = Matrix([['a', 2, 5], [4, 5, 1], [6, 8, 7]])
matrix9 = Matrix([[5, 6, [1, '32']], [3, 3, 1], [3, 5, 6]])
matrix10 = matrix8 + matrix9                                       # example of non-numerical elements of matrices

matrix7 = matrix3 + matrix6                                        # example of different sized matrices
