# HW5 - Task № 5
# Create a (programmatically) text file, write a set of numbers
# separated by spaces into it programmatically. The program should
# calculate the sum of the numbers in the file and display it on
# the screen.
f, result = True, 0
with open('Text_5.txt', 'w', encoding='UTF-8') as file:
    line = input('Enter line of numbers divided by spaces:\n')
    try:
        for itm in line.split():
            itm = float(itm)
        file.writelines(line)
    except ValueError:
        print('Enter correct data')
        f = False
if f:
    try:
        with open('Text_5.txt', 'r', encoding='UTF-8') as file_:
            line = line.split()
            for itm in line:
                result += float(itm)
            print(result)
    except FileNotFoundError:
        print('\nThe required file does not exist')
