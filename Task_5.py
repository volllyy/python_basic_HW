#HW - Task № 5
revenue = input('Enter the revenue value of the firm:\n')
costs = input('Enter the costs of the firm:\n')
if revenue.isdigit() and costs.isdigit():
    if int(revenue) > int(costs):
        print('The firm is working with profit')
        prof = int(revenue) - int(costs)
        Prof_m = (int(prof) / int(revenue)) * 100
        print('Profit margin of the firm is:', Prof_m,'%')
        num_workers = input('Enter the amount of workers in the firm:\n')
        if num_workers.isdigit():
            print('The profit per 1 worker is:', int(prof) / int(num_workers))
        else:
            print('Enter correct data please!')
    elif int(revenue) == int(costs):
        print('The firm is working with 0 profit')
    else:
        print('The firm is working with loses')
else:
    print('Enter correct data please!')
