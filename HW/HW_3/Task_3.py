# HW3 - Task № 3
def sum_2_max(var_1: float, var_2: float, var_3: float) -> float:
    """
    This function takes 3 float values and return sum of 2 max.
    :param var_1: float
    :param var_2: float
    :param var_3: float
    :return: float sum of two highest from var_1, var_2, var_3
    """
    try:
        var_1 = float(var_1)
        var_2 = float(var_2)
        var_3 = float(var_3)
    except ValueError:
        print('Enter all 3 digits please')
        return ''
    if (var_1 >= var_3) and (var_2 > var_3):
        result = var_1 + var_2
    elif (var_3 >= var_1) and (var_1 > var_2):
        result = var_1 + var_3
    else:
        result = var_2 + var_3
    return result

x = input('Enter 1st variable:\n')
y = input('Enter 2nd variable:\n')
z = input('Enter 3ed variable:\n')
print(sum_2_max(x, y, z))

