# HW2 - Task № 2
print('Enter items for the list:')
user_input = input()
my_list = user_input.split(' ')
for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
print('Result:',my_list)
