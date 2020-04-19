# HW3 - Task № 2
def info_func(name: str, surname: str, birth: int, city: str, email: str, number: str) -> str:
    """
    The function accepts several parameters describing
    the user’s data: name, surname, year of birth, city
    of residence, email, phone and displays user data in one line.
    :param name: str
    :param surname: str
    :param birth: int
    :param city: str
    :param email: str
    :param number: int
    :return: str all parameters in one line
    """
    try:
        birth = int(birth)
    except ValueError:
        print('Enter correct year of birth')
        return ''
    try:
        number = int(number)
    except ValueError:
        print('Enter correct year of birth')
        return ''
    print(f"Name - {name}; Surname - {surname}; "
          f"Birth - {birth}; City - {city}; Email - {email}; "
          f"Phone number - {number}")
    return ''


name_f = input('Enter name:\n')
surname_f = input('Enter surname:\n')
birth_f = input('Enter year of birth:\n')
city_f = input('Enter city:\n')
email_f = input('Enter email:\n')
number_f = input('Enter phone number:\n')
#print(info_func(name_f = 'Vova', surname_f = 'Antonenko',
#      birth_f = '1997', city_f = 'Moscow', email_f = 'volllyy@gmail.com,
#      number_f = 89998887766))
print(info_func(name_f, surname_f, birth_f, city_f, email_f, number_f)')
