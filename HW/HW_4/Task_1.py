# HW4 - Task № 1
from sys import argv


def salary_func() -> float:
    """
    This is employee payroll function. Formula: (production in hours * rate per hour) + bonus.
    :return: float salary
    """
    _, time, salary, bonus = argv
    try:
        final_salary = float(time) * float(salary) + float(bonus)
        print(f'Final salary is {final_salary}')
    except ValueError:
        return print('Enter the real numbers please')


salary_func()
