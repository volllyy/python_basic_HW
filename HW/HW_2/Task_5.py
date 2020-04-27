# HW2 - Task № 5
my_list = [7, 5, 4, 3, 3, 2]
new = input('Enter a natural number:\n')
if new.isdigit():
    new = int(new)
    max_in_list = max(my_list)
    if new > int(max_in_list):
        my_list.insert(0, new)
    elif new in my_list:
        my_list.insert(-my_list[::-1].index(new), new)
    else:
        my_list.append(new)
    print('Result:', my_list)
else:
    print('Enter the correct data')
