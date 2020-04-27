# HW5 - Task № 2
# Create a text file (not software), save several
# lines in it, count the number of lines, the number
# of words in each line.
try:
    with open('Text_2', 'r', encoding='UTF-8') as file:
        x, i = 0, 1
        for line in file:
            x = x + line.count('\n')
            if line.strip():
                print(f'Words in {i} line: {line.count(" ") + 1}')
            i += 1
        print(f'\nNumber of lines in file "Text_2.txt": {x + 1}')   #empty line is also line here
except IOError:
    print('\nAn I / O error has occurred!')
