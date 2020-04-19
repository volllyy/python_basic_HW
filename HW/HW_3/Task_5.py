# HW3 - Task № 5
def sum_func() -> int:
    """
    The program asks the user for a string of numbers separated by a space.
    When you press Enter, the sum of the numbers should be displayed.
    The user can continue to enter numbers separated by a space and press Enter again.
    The sum of the newly entered numbers will be added to the already calculated
    amount. But if a special character (Stop or stop) is entered instead of a number, the program
    ends. If a special character is entered after several numbers, then first you
    need to add the sum of these numbers to the previously received amount and then
    complete the program.
    :return: Int // Return sum of all digits in all strings entered by user.
    """
    data = True
    next_enter = True
    sum_total = 0
    while next_enter and data:
        sum_inter = 0
        my_list = input('Enter string of digits\n').split(' ')
        for itm in range(len(my_list)):
            if my_list[itm] == 'stop' or my_list[itm] == 'Stop':
                next_enter = False
                break
            elif my_list[itm].isdigit():
                sum_inter = sum_inter + int(my_list[itm])
            elif my_list[itm] == '':                            #if user in the end of the string add Space
                my_list = my_list.pop(-1)                       #delete the last element equal to the empty element
                sum_inter = sum_inter + int(my_list[itm])
            else:
                print('Enter correct data')
                data = False
                break
        sum_total = sum_total + int(sum_inter)
        print('Intermediate sum of 1 line is', sum_inter)
    print('Final sum of all strings', sum_total)


sum_func()
