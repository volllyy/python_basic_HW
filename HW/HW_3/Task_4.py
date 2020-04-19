# HW3 - Task № 4
def exp_func(x: float, y: int) -> float:
    """
    The function takes two values, a real positive
    number x and a negative integer y.
    The function raises x to the power of y.
    :param x: float
    :param y: int negative
    :return: float x^y
    """
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('Enter correct data please')
        return ''
    if y < 0:
        i = abs(y)
        a = float(x)
        while i != 1:
            a = float(x) * a
            i -= 1
        result = 1 / a
        return result
    else:
        print('Enter negative y')
        return ''


x_1 = input('Enter real positive number x which you want to raise to the power of y\n')
y_1 = input('Enter negative integer power y\n')
print(exp_func(x_1, y_1))


# # Simpler version with operator **
# def exp_func_1(x: float, y: int) -> float:
#     try:
#         x = float(x)
#         y = int(y)
#     except ValueError:
#         print('Enter correct data please')
#         return ''
#     if y < 0:
#         result = 1 / (x ** abs(y))
#         return result
#     else:
#         print('Enter negative y')
#         return ''
#
#
# x_1 = input('Enter real positive number x which you want to raise to the power of y\n')
# y_1 = input('Enter negative integer power y\n')
# print(exp_func_1(x_1, y_1))
