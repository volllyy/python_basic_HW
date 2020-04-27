# HW5 - Task № 1
# Create a program file in text format, write to it
# line by line the data entered by users. The end of
# data entry is indicated by an empty line.

with open('Text_1.txt', 'w', encoding='UTF-8') as file:
    try:
        while True:
            line = input('Enter line of text(enter only '
                         '"enter" to stop entering:\n')
            file.writelines(line + '\n')
            if not line:
                break
    except IOError:
        print('An I / O error has occurred!')
        pass
