# HW3 - Task № 5
def int_func(x: str) -> str:
    """
    This function takes a word from lowercase latin letters
    and returns it, but with a capital first letter.
    :param x: str word with lowercase latin letter
    :return: srt word with capital first latin letter
    """
    x = x.title()
    return x


my_list = input('Enter the string consists of lowercase latin letters\n').split(' ')
result = str()
for el in my_list:
    el = str(el)
    result = result + ' ' + int_func(el)
print(result[1:len(result)])


