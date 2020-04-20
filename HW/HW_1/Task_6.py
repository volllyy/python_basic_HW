#HW1 - Task № 5
a = input('Enter the number of kilometers '
          'that the athlete ran on the first day:\n')
b = input('Enter the target result of '
          'kilometers in one day:\n')
if a.isdigit() and b.isdigit():
    i = 1                                                   #Counter from the first day of running
    growth = 1.1                                            #Growth by 10% by each day
    while float(a) <= float(b):
        a = float(a) * growth
        i += 1
    print('On the ', i,'`th day atlete achieved a result '
                       'of at least 3 km', sep = '')
else:
    print('Enter the correct result please!')
