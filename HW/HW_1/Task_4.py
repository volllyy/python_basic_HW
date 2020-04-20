#HW1 - Task № 4
number = input('Enter any digit:\n')
if number.isdigit():
    i = len(number)
    t = -1
    while i != 0:
        digit = int(number) % 10
        number = int(number) // 10
        if digit > t:
            t = digit
        i = i - 1
    print('The largest digit in the entered number is:', t)
else:
    print('Enter the real number please!')
