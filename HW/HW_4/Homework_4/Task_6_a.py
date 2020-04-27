# HW4 - Task № 6_a
# a) Script with an infinite iterator generating
# integers starting from the specified.
from sys import argv
from time import sleep
from itertools import count
_, n = argv
try:
    n = int(n)
except ValueError as e:
    print(e)
for i in count(n, 1):
    print(i)
    sleep(1)        #для наглядности получаемого результата
