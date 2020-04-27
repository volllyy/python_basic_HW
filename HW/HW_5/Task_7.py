# HW5 - Task № 7
# Create (not programmatically) a text file in which each
# line should contain information about the company: name,
# form of ownership, revenue, costs.

# It is necessary to read the file line by line, calculate
# the profit of each company, as well as the average profit.
# If the company received losses, do not include it in the
# calculation of average profit.

# Next, implement the list. It should contain a dictionary
# with firms and their profits, as well as a dictionary with
# average profit. If the company received losses, also add it
# to the dictionary (with the value of losses).

# Save the resulting list as a json object to the corresponding file.
import json
try:
    with open('Text_7', 'r', encoding='UTF-8') as file:
        i, average = 0, 0
        my_list_ = []
        my_dict, my_dict_ = {}, {}
        f = True
        my_list = file.readlines()
        if my_list:
            for itm in my_list:
                name, own_ship, revenue, costs = itm.split()
                try:
                    profit = float(revenue) - float(costs)
                    if profit >= 0:
                        average += profit
                        i += 1
                    my_dict[name] = profit
                except ValueError:
                    print('\nEnter correct data in file Text_7')
                    f = False
                    break
            if f:
                try:
                    average = ('{:.3f}'.format(average / i))
                    my_dict_['Average profit'] = average
                except ZeroDivisionError:
                    print('\nZero division because no firms with positive profit')
                    f = False
        else:
            print('\nNo data in file')
            f = False
except IOError:
    print('An I / O error has occurred!')
    f = False
if f:
    my_list_.append(my_dict)
    my_list_.append(my_dict_)
    j_data = json.dumps(my_list_)
    print(f'\nThe final list is: {my_list_}')
    with open('data_7.json', 'w', encoding='UTF-8') as file:
        file.write(j_data)
