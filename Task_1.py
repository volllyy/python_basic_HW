#HW - Task № 1
year = 2020
temperature = 10.5
month = 'April'
print(year,'/', temperature,'Cº /', month)
name = input('What`s your name?\n')
surname = input('What`s your surname?\n')
age = input('How old are you?\n')
number = input('What is your phone number? (Wright down without + and spaces, '
               'just country code and tel.namber)\n')
if name.isdigit() or surname.isdigit():
    print('Enter correct information about name and surname please!')
else:
    print('Name:', name,'/ Surname:', surname)
if not age.isdigit() or not number.isdigit():
    print('Enter correct information about age and phone number please!')
else:
    print('Age:', age,'/ Phone number: +', number)
