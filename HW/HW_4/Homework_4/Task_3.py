# HW4 - Task № 3
# For numbers between 20 and 240, find numbers that are multiples of 20 or 21.
print(f'All numbers from 20 to 240 multiples of 20 or 21 are:'
      f'{[el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]}')
