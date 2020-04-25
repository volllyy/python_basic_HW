# HW4 - Task № 7
"""
Implement the generator using a function with the yield keyword
that creates the next value. When a function is called, a generator
object must be created. The function should be called as follows:
for el in fib_gen (). The function is responsible for obtaining
the factorial of the number, and in the loop it is necessary to display
only the first 15 numbers.
"""
from itertools import count
from math import factorial


def fibo_gen() -> int:
    """
    The function is responsible for obtaining
    the factorial of the number.
    :return: int factorial of the number
    """
    for el in count(1):
        yield factorial(el)


for i, itm in enumerate(fibo_gen(), 1):
    if i <= 15:
        print(i, itm)
        i += 1
    else:
        break
