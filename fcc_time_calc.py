def add_time(start_time, duration, week_start):
    # Convert start_time to an integer
    # day = "AM"
    # night = "PM"
    # if start_time.find(day):
    #     print("AM")
    # else:
    #     print("PM")

    # Split start_time into numbers and letters
    no_letters = start_time.split(" ") 
    # Split no_letters into two variables, start_time and time_of_day
    time_of_day = no_letters[1]
    start_time = no_letters[0]
    start_time = start_time.split(":")
    start_hour = int(start_time[0])
    start_minutes = int(start_time[1])

    # if start_time.find('PM'):
    #     print("AM")
    # else:
    #     print("Find another way")
    
    # if start_hour < 11:
    #     mil_time = (start_hour + 12)
    print(f'Time of day is {time_of_day}')
    print(f'Start time is {start_time}')
    print(f'The start hour is {start_hour}')
    print(f'The start minutes is {start_minutes}')




add_time("10:59 PM", 0, 0)