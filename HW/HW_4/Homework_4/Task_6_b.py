# HW4 - Task № 6_b
# b) Script with an infinite iterator repeating
# the elements of a list defined in advance.
from time import sleep
from itertools import cycle
from sys import argv
_, *my_list = argv
# my_list = [1, 2, 3, 'Once again']
while True:
    count = 0
    for i in cycle(my_list):
        if count == len(my_list):
            break
        print(i)
        sleep(1)                    #для наглядности получаемого результата
        count += 1
