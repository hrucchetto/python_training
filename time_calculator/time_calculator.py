def add_time(start: str, duration: str, start_day: str= None) -> str:

    dow_dict = {
        'monday': 1,
        'tuesday': 2,
        'wednesday': 3,
        'thursday': 4,
        'friday': 5,
        'saturday': 6,
        'sunday': 0
    }

    start_time, midday = start.split(' ')

    if midday == "PM":
        if int(start_time.split(':')[0]) == 12:
            start_hs =  int(start_time.split(':')[0]) + int(start_time.split(':')[1]) / 60
        else:
            start_hs =  12 + int(start_time.split(':')[0]) + int(start_time.split(':')[1]) / 60
    else:
        if int(start_time.split(':')[0]) == 12:
            start_hs =  int(start_time.split(':')[1]) / 60
        else:
            start_hs =  int(start_time.split(':')[0]) + int(start_time.split(':')[1]) / 60
    
    duration_hs = int(duration.split(':')[0]) + int(duration.split(':')[1]) / 60

    new_time_hs = start_hs + duration_hs
    print(new_time_hs)
    
    num_extra_days = int(new_time_hs / 24)
    new_time_int = new_time_hs % 24
    print(new_time_int)


    if int(new_time_int) == 0:
        new_time = '12:' + str(round((new_time_int - int(new_time_int)) * 60)).rjust(2, '0') + ' AM'
    elif int(new_time_int) == 12:
        new_time = str(int(new_time_int)) + ':' + str(round((new_time_int - int(new_time_int)) * 60)).rjust(2, '0') + ' PM'
    elif int(new_time_int) > 12:
        new_time = str(int(new_time_int) - 12) + ':' + str(round((new_time_int - int(new_time_int)) * 60)).rjust(2, '0') + ' PM'
    else:
        new_time = str(int(new_time_int)) + ':' + str(round((new_time_int - int(new_time_int)) * 60)).rjust(2, '0') + ' AM'

    if start_day:
        current_day = dow_dict[start_day.lower()]
        new_day = [i for i in dow_dict if dow_dict[i] == (current_day + num_extra_days) % 7][0]
        new_time = new_time + f', {new_day.capitalize()}'

    if num_extra_days == 0:
        return new_time
    elif num_extra_days >= 2:
        return new_time + f' ({num_extra_days} days later)'
    else:
        return new_time + f' (next day)'

x = add_time("11:40 AM", "0:25")
print(x)