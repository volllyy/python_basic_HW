# HW4 - Task № 5
# The list should include even numbers from 100 to 1000 (including borders).
# It is necessary to obtain the result of computing the product of all elements of the list.
from functools import reduce
my_list = [el for el in range(100, 1001) if not el & 1]
multiple = reduce(lambda x, y: x * y, my_list)
print(f'All even numbers between 100 and 1000:\n{my_list},\n'
      f'Multiple of all even numbers between 100 and 1000:\n{multiple}')
# print(f'Multiple of all even numbers between 100 and 1000:\n{multiple}')
