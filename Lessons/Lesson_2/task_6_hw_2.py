# n = input('Enter the amount of tuples you want:\n')
# if n.isdigit():
#     n = int(n)
#     my_list = []
#     my_list_f = []
#     for i in range(0, n, 1):
#         my_str = input('Enter |Name|-|Price|-|Amount|-|Unit of calculation| (divided by spaces)\n')
#         my_list = my_str.split(' ')
#         name_f = my_list[0]
#         price_f = my_list[1]
#         amount_f = my_list[2]
#         unit_f = my_list[3]
#         my_dict = dict(Name=name_f, Price=price_f, Amount=amount_f, Unit=unit_f)
#         # print(my_dict)
#         my_tuple = (i+1, my_dict)
#         # print(my_tuple)
#         my_list_f.append(my_tuple)
# else:
#     print('Enter correct data')
# print(my_list_f)