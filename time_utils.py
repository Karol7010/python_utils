from datetime import datetime

def working_days_till_eom(number_of_holidays = 0):
    day = int(str(datetime.now())[8:10])
    month = int(str(datetime.now())[5:7])
    year = int(str(datetime.now())[0:4])
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] if year == 0 else [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_month = days_in_month[month-1]
    day_of_week = (datetime.now()).weekday()+1 # Monday = 1,...
    working_days_left = 0
    for i in range(days_in_month-day):
        if day_of_week == 8:
            day_of_week = 1
        if day_of_week in [1, 2, 3, 4, 5]:
            working_days_left += 1
        day_of_week += 1
    return working_days_left - number_of_holidays
