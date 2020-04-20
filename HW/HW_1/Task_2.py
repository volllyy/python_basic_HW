#HW1 - Task № 2
time = input('Enter time in seconds:\n')
t_hour = 3600                                       #seconds in 1 hour
t_day = 86400                                       #seconds in 1 day
if time.isdigit():
    if int(time) >= 86400:
        time = int(time) - 86400
    hours = int(time) // 3600
    minutes = (int(time) - (hours * 3600)) // 60
    seconds = (int(time) - (hours * 3600)) % 60
    time_result = 'Time is {0:>02}:{1:>02}:{2:>02}'\
        .format(hours, minutes,seconds)
    print(time_result)
else:
    print('Enter correct data please!')
