# HW5 - Task № 3
# Create a text file "Text_3" (not programmatically), write
# down the names of employees and their salaries line by line.
# Determine which of the employees has a salary of less than
# 20 thousand, display the names of these employees. Perform
# a calculation of the average employee income.
i, salary = 0, 0
surname = []
f = True
try:
    with open('Text_3', 'r', encoding='UTF-8') as file:
        my_list = file.read().split('\n')
        if my_list != ['']:
            for itm in my_list:
                if itm != '':
                    itm = itm.split(' ')
                    try:
                        if float(itm[-1]) < 20000:
                            surname.append(itm[0])
                        salary += float(itm[-1])
                        i += 1
                    except ValueError:
                        print('Enter correct data in file Text_3.txt!')
                        f = False
                        break
        else:
            print('Enter data in file Text_3.txt please')
            f = False
        if f:
            print(f'Salary less than 20k have: {surname}, average salary is: {salary / i}')
except FileNotFoundError:
    print('\nThe required file does not exist')
