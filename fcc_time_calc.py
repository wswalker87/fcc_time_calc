def add_time(start_time, duration, week_start = "" ):
    # Split start_time into numbers and letters
    no_letters = start_time.split(" ")
    new_day = 0

    # Split no_letters into two variables, start_time and time_of_day
    time_of_day = no_letters[1].upper()
    start_time = no_letters[0]
    start_time = start_time.split(":")
    start_hour = int(start_time[0])
    start_minutes = int(start_time[1])

    # Begine working on the management of days.
    # Assign days of the week a numerical value in a dictionary. Remember that the week_start is all lower case already. 
    # Get day of the week, make it upper-case no matter what the input was
    week_start_lower = week_start.lower()

    day_mapping = {
        'sunday': 1,
        'monday': 2,
        'tuesday': 3,
        'wednesday': 4,
        'thursday': 5,
        'friday': 6,
        'saturday': 7
    }
    # Discover what day of the week was supplied if any
    day_value = day_mapping.get(week_start_lower)

    # Might have to use this later to get python to stop dropping the leading 0
    # formatted_minutes = str(start_minutes).zfill(2) *OR* I can use ":02d" on my variable in the fstring to require at least two decimals

    # Get duration into an integer
    duration = duration.split(":")
    duration_hours = int(duration[0])
    duration_minutes = int(duration[1])

    

    if time_of_day == "AM":
        mil_start_hours = start_hour
        mil_start_minutes = start_minutes
        if mil_start_hours == 12:
            mil_start_hours = 0
    elif time_of_day == "PM":
        mil_start_hours = start_hour + 12
        mil_start_minutes = start_minutes
        if mil_start_hours == 24:  # Give a way to not have 24 on the clock since it goes from 23:59 to 00:00
            mil_start_hours = 0

    # Add duration to start time
    mil_final_hours = mil_start_hours + duration_hours
    mil_final_minutes = mil_start_minutes + duration_minutes
        # Handle any sum of start and duration that goes past midnight, maybe increase a count for new_day here, but I need to think about minutes as well.
    # Testing a while loop for going past midnight
    new_day = 0
    # while mil_final_minutes >= 60 or mil_final_hours >= 24:
    #     day_minutes_remainder = mil_final_minutes % 60
    #     mil_final_minutes = 0 + day_minutes_remainder

    #     day_hour_remainder = mil_final_hours % 24
    #     mil_final_hours = 0
    #     new_day += 1
    
    # new_day += mil_final_hours // 24
    
    
    
    
    if mil_final_minutes >= 60: # changed from 59 to 60. Make sure all the use cases pass
        day_minutes_remainder = mil_final_minutes - 60
        mil_final_minutes = 0 + day_minutes_remainder
        mil_final_hours += 1
        
    if mil_final_hours >= 24: # changed from 25 to 24. Make sure all the use cases pass
        day_hour_remainder = mil_final_hours - 24
        mil_final_hours = 0 + day_hour_remainder
        new_day += 1

    # Convert back to 12 hour time
    if mil_final_hours >= 0 and mil_final_hours <= 11:
        final_time_of_day = "AM"
    elif mil_final_hours >= 12:
        final_time_of_day = "PM"
    norm_final_hours = mil_final_hours if mil_final_hours <= 12 else mil_final_hours - 12
    norm_final_minutes = mil_final_minutes

    # Determine new day, based on the week_start and new_day counts
    
    if week_start:
        new_day_value = (day_value + new_day - 1) % 7 + 1
        new_day_name = [ k for k, v in day_mapping.items() if v == new_day_value][0]
    if new_day == 1:
        days_later = "next day"
    elif new_day >= 2:
        days_later = f'{new_day} days later'


    






# Testing with print statements. Don't forget to add return statements for the final testing. 
    print(f'Normal final time is {norm_final_hours}:{norm_final_minutes:02d} {final_time_of_day}')
    print(f"The numerical value for {week_start} is {day_value}.")
    print(f'New day count is {new_day}')
    print(f'The new day is {new_day_name.capitalize()}')

add_time("6:30 PM", "205:12", "Monday")