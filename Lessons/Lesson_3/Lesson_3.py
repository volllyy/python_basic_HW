# # b = 0
# # c = 12
# # my_list = [1, 2, 3, 4, 5]
# # try:
# #     a = my_list[c] / b
# # except ZeroDivisionError:
# #     print('Zero division')
# # except IndexError:
# #     print('Out of range')
# """
# finally:
# #     print('Always done')
#
# Отлов всех ошибок
# # except Exception:
# #     print('All errors')
# """
#
# # Functions
#
# # def my_func(x: int, y:float) -> float:
# #     """
# #     Это функция которая что-то делает
# #     :param x: int
# #     :param y: float
# #     :return: float result of calculation
# #     """
# #     result = x ** y
# #     return result
# #     print('функция поработала', result)
#
# def my_sum(var_list: list) -> float:
#     ### 1
#     # result = 0
#     # for itm in var_list:
#     #     result += itm
#     # return result
#     ###2
#     # if not var_list:
#     #     return 0
#     # x = var_list.pop()
#     # return x + my_sum(var_list)
#     ###3
#     return var_list[0] + my_sum(var_list[1:]) if var_list else 0
#
#
my_list = [1, 2, 3, 4, 5]
# my_var = my_sum(my_list)
# print(my_var)
# print(my_list)
# # my_var = my_func(2, 5)
# # print(my_var)
#
#
def my_tempo(a):
    return a ** 2

temp = map(my_tempo, my_list)

print(list(temp))


# def my_map(func, var_iterable) -> list:
#     result = []
#     for itm in var_iterable:
#         result.append(func(itm))
#     return result
#
# print(my_map(my_tempo, my_list))

def my_map(func, var_iterable) -> list:

    print('sds')
    for itm in var_iterable:
        print('ds')
        yield func(itm)
        print('ds')

# print(list(temp))

# for itm in temp:
#     print(itm)
temp = map(my_tempo, my_list)

print(next(temp))
print(next(temp))


