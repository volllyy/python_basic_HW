# HW2 - Task № 6 ***
list_goods = []
i = 0
while input("Do you want to add a position to the list? "
            "Enter y/n:\n") == 'y':
    parameters = {}                                         #dict of different paremeters like: name, price, quantity, unit
    while input("Do you want to add product parameters? "
                "Enter y/n:\n") == 'y':
        my_key = input("Enter parameter(key) of the product:\n")
        my_value = input("Enter value of the parameter(key):\n")
        parameters[my_key] = my_value
    i += 1
    list_goods.append(tuple([i, parameters]))
print('[')
print(*list_goods, sep='\n')
print(']\n')
dict_analytics = {}
for good in list_goods:
    for my_key, my_value in good[1].items():
        if my_key in dict_analytics:
            dict_analytics[my_key].append(my_value)
        else:
            dict_analytics[my_key] = [my_value]
print(dict_analytics)

