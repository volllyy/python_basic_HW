# HW3 - Task № 1
def dev_func(x: float, y: float) -> float:
    """
    This function make the division of X by Y
    :param x: float dividend
    :param y: float divider
    :return: float result x/y
    """
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print('Enter correct data - digits')
        return ''
    try:
        x_y = float(x) / float(y)
    except ZeroDivisionError:
        print('Zero division, enter another divider - (b)')
        return ''
    return x_y


a = input('Enter dividend\n')
b = input('Enter divider\n')
print(dev_func(a, b))
