# HW2 - Task № 4
my_str = input('Enter a string with some words separated by a space:\n')
my_list = my_str.split(' ')
i = 1
for el in my_list:
    if len(el) <= 10:
        print(f'{i}) {el:<10}')
        i += 1
    else:
        print(f'{i}) {el[0:10]:<10}')
        i += 1
