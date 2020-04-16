# HW2 - Task № 3
n = input('Enter the mouth number:\n')
if (n.isdigit()) and (12 >= int(n) >= 1):
    n = int(n)
    mouth_dict = {1: 'Winter', 2: 'Winter', 3: 'Winter',
                  4: 'Autumn', 5: 'Autumn', 6: 'Autumn',
                  7: 'Summer', 8: 'Summer', 9: 'Summer',
                  10: 'Spring', 11: 'Spring', 12: 'Spring'
                  }
    mouth_list = list(mouth_dict.values())
    for i, el in enumerate(mouth_list):
        if i == n - 1:
            print('The month entered refers to the', mouth_list[i])
            break
else:
    print('Enter correct data please')
