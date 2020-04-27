#HW - Task № 3
n = input('Enter any digit please:\n')
if n.isdigit():
    str_1 = n
    str_2 = n * 2
    str_3 = n * 3
    result = int(str_1) + int(str_2) + int(str_3)
    print('The result is:', result)
else:
    print('Enter the real number please!')