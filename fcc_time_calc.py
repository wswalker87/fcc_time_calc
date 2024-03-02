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

    # Begin working on the management of days.
    # Assign days of the week a numerical value in a dictionary. Remember that the week_start is all lower case already. 
    
    day_mapping = {
        'sunday': 0,
        'monday': 1,
        'tuesday': 2,
        'wednesday': 3,
        'thursday': 4,
        'friday': 5,
        'saturday': 6
    }

    # Get the actual day of the calculation
    #current_day = (day_mapping['sunday'] + new_day) % 7
    
    # Get day of the week, make it upper-case no matter what the input was
    week_start_lower = week_start.lower()
    current_day = day_mapping.get(week_start_lower, 0)

    # Get duration into an integer
    duration = duration.split(":")
    duration_hours = int(duration[0])
    duration_minutes = int(duration[1])
    
    # Convert start time to 24-hour format
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
    # Had to move the new_day variable INTO the while loop, as well as have it outside in front of the loop to prevent the increment from not working.

  
 
    while mil_final_minutes >= 60 or mil_final_hours >= 24:
        mil_final_hours += mil_final_minutes // 60
        mil_final_minutes %= 60
        # Increment for days that runneth over. 
        new_day += mil_final_hours // 24
        mil_final_hours %= 24

    # Print statements for debugging
    #print(f"Debug: mil_final_hours = {mil_final_hours}, new_day = {new_day}")



    norm_final_hours = mil_final_hours % 12 if mil_final_hours % 12 != 0 else 12
    norm_final_minutes = mil_final_minutes

    if mil_final_hours >= 12:
        final_time_of_day = "PM"
    else:
        final_time_of_day = "AM"
        

    # Determine new day, based on the week_start and new_day counts
    new_day_name = ""
    new_day_value = 0
    if week_start:
        new_day_value = (current_day + new_day) % 7
        new_day_name = [ k for k, v in day_mapping.items() if v == new_day_value][0]

    # Check if it's the next day or multiple days later
    if new_day == 0 and norm_final_hours < 12:
        days_later = ""  # Same day, before noon
    else:
        days_later = "next day" if new_day == 1 else f"{new_day} days later"

    # Print for testing
    # if week_start == "" and new_day == 0:
    #     print(f'a{norm_final_hours}:{norm_final_minutes:02d} {final_time_of_day}')
    # elif week_start and new_day:
    #     print(f'c{norm_final_hours}:{norm_final_minutes:02d} {final_time_of_day}, {new_day_name.capitalize()} ({days_later})')
    # elif week_start:
    #     print(f'b{norm_final_hours}:{norm_final_minutes:02d} {final_time_of_day}, {new_day_name.capitalize()}')
    # elif new_day >= 1:
    #     print(f'd{norm_final_hours}:{norm_final_minutes:02d} {final_time_of_day} ({days_later})')
    
    # Returns for the unit testing
    if week_start == "" and new_day == 0:
        return f'{norm_final_hours}:{norm_final_minutes:02d} {final_time_of_day}'
    elif week_start and new_day:
        return f'{norm_final_hours}:{norm_final_minutes:02d} {final_time_of_day}, {new_day_name.capitalize()} ({days_later})'
    elif week_start:
        return f'{norm_final_hours}:{norm_final_minutes:02d} {final_time_of_day}, {new_day_name.capitalize()}'
    elif new_day >= 1:
        return f'{norm_final_hours}:{norm_final_minutes:02d} {final_time_of_day} ({days_later})'
   

# add_time("11:43 PM", "24:20", "tueSday") # Should return 12:03 AM, Thursday (2 days later) and actually returns 12:03 AM, Thursday (2 days later). Correct.
    
# add_time("6:30 PM", "205:12") # Should return 7:42 AM (9 days later) and returns 7:42 AM (9 Days later). Right, but the spacing looks off. 
    
# add_time("3:00 PM", "3:10") # Should Return: 6:10 PM and actually returns 6:10 PM. Correct.

# add_time("11:30 AM", "2:32", "Monday") # Should return 2:02 PM, Monday and actually returns 2:02 PM, Monday (). Wrong. Empty parentheses need to go.

# add_time("11:43 AM", "00:20") # Should return 12:03 PM and actually returns 12:03 AM. Mostly correct. Should just be "12:03 PM"

# add_time("10:10 PM", "3:30") # Should return 1:40 AM (next day) and actually returns 1:40 AM, (next day). Wrong because of the comma.

add_time("2:59 AM", "24:00", "saturDay") #should return 2:59 AM, Sunday (next day).

add_time("11:59 PM", "24:05", "Wednesday") #should return "12:04 AM, Friday (2 days later)".

add_time("8:16 PM", "466:02", "tuesday") #should return 6:18 AM, Monday (20 days later).