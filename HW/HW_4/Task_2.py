# HW4 - Task № 2
# It is necessary to display elements of the initial
# list whose values are greater than the previous element.
# my_list_ = [8, 3, 4, 1, 2, 132, 111111, 0, -2, -1, 32, 3]
my_list_ = [1, 2]
new_my_list = [el for n, el in enumerate(my_list_) if n and my_list_[n - 1] < my_list_[n]]
print(f'New list is: {new_my_list}')
