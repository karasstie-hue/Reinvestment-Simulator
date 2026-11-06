month_int = 0.005
ann_int = month_int*12

trial_dur = 50

print('Annual Interest Reinvestment Simulation:')
month = 0
fund = 100
for i in range(trial_dur):
    month = month + 12
    year = month / 12
    fund = fund * (1+ann_int)
    print (f'Year: {year:<5} Fund: {fund:<5.2f}')

print('\n\nMonthly Interest Reinvestment Simulation:')
month = 0
fund = 100
for i in range(trial_dur*12):
    month = month + 1
    year = month / 12
    fund = fund * (1+month_int)
    if round(year) == year: 
        print (f'Year: {year:<5} Fund: {fund:<5.2f}')
