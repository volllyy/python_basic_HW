# HW5 - Task № 4
# It is necessary to write a program that opens a file for reading and
# reads data line by line. In this case, English numerals should be
# replaced by Russian. A new block of lines should be written to a new text file.

ru = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_list = []
f = True
try:
    with open('Text_4', 'r', encoding='UTF-8') as file:
        try:
            for itm in file:
                itm = itm.split(' ', 1)
                my_list.append(ru[itm[0]] + ' ' + itm[1])
        except KeyError:
            print('\nEnter correct data')
            f = False
except FileNotFoundError:
    print('\nThe required file does not exist')
if f:
    with open('Text_4_result.txt', 'w', encoding='UTF-8') as file_2:
        i = 0
        for i in range(len(my_list)):
            file_2.writelines(my_list[i])
            i += 1
