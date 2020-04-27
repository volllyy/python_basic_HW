# HW5 - Task № 6
# It is necessary to create a (non-software) text file, where each
# line describes the subject and the presence of lectures, practical
# and laboratory exercises on this subject and their number. It is
# important that for each subject not all classes are required.
# Generate a dictionary containing the name of the subject and the total
# number of classes on it. Display the dictionary on the screen.
# — this symbol indicates no hours
my_dict, f = {}, True
with open('Text_6', 'r', encoding='UTF-8') as file:
    try:
        for line in file:
            subject, hours = line.split(':')
            lecture, practice, lab = hours.split()
            try:
                if lecture == '—':
                    lecture = 0
                else:
                    lecture = lecture[0:lecture.find('(')]
                if practice == '—':
                    practice = 0
                else:
                    practice = practice[0:practice.find('(')]
                if lab == '—':
                    lab = 0
                else:
                    lab = lab[0:lab.find('(')]
                my_dict[subject] = int(lecture) + int(practice) + int(lab)
            except ValueError:
                print('Enter data in file Text_6 correctly')
                f = False
                break
    except IOError:
        print('An I / O error has occurred!')
        f = False
if f:
    print(f'Dictionary containing the name of the subject '
          f'and the total number of classes on it - \n {my_dict}')
