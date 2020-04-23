from itertools import cycle
from time import sleep
#math statistics
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def my_cycle(my_iter):
    c = len(a)
    while True:
        idx = 0
        while idx < c:
            yield my_iter[idx]
            idx += 1



for itm in my_cycle(a):
    print(itm)
    sleep(0.5)



# from my_test.my_module import test
#
# print(test(6, 6))
#
# print(__name__)

# def time(x):
# return x ** 2
# start = tm()
# for itm in range(10):
#     print(itm)
#     tm.sleep(1)
# end = tm()
# print(end - start)
#
# import my_test.my_module
# #or from my_module import test
#
# print(my_module.test(6, 6))
