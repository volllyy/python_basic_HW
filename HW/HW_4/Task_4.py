# HW4 - Task № 4
# A list of numbers is presented; display a new list
# in which there will be all the elements of the original
# list without repetition, while maintaining the order in
# which they appear in the original list.
my_list = [9, 8, 9, 8, 7, 6, 7, 6, 5, 4, 5, 4]
my_list = [1, 2, 3, 4, 1, 2]
# Bad because we gen new list for each el
# my_new_list = [el for n, el in enumerate(my_list_) if el not in my_list_[:n]]
# print(my_new_list)

my_new_list_1 = [el for el in my_list if my_list.count(el) == 1]
print(my_new_list_1)
