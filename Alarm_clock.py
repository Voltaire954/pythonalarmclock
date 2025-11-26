# #ABORIGINAL alarm clock


import time            # Built-in Python module for time-related functions (sleep, etc.)
import datetime        # Built-in module for working with dates and times
from zoneinfo import ZoneInfo  # Provides time zone support (Python 3.9+)

def set_alarm(alarm_time):
    """
    Runs a simple alarm loop that checks the current Eastern Time (ET)
    every second until it matches the user-specified alarm time.
    """
    print(f"Alarm set for {alarm_time}")
    is_running = True  # Controls the loop; alarm runs until set to False

    while is_running:
        # Get the current time in the Eastern Time zone (EST/EDT)
        now = datetime.datetime.now(ZoneInfo("America/New_York"))

        # Format the time in 12-hour format with AM/PM (e.g., "07:30:00 PM")
        current_time = now.strftime("%I:%M:%S %p")

        print(current_time)  # Display the current time to the user

        # If the current time matches the alarm time, trigger alarm
        if current_time == alarm_time:
            print("WAKE UP!!!")
            is_running = False  # Stops the while-loop (alarm completes)

        time.sleep(1)  # Wait 1 second before checking the time again


# Ensures this block only runs when the file is executed directly
if __name__ == '__main__':
    # Ask user for alarm input in the AM/PM format the clock uses
    alarm_time = input("Enter the alarm time (HH:MM:SS AM/PM): ")

    # Call the function and start the alarm clock
    set_alarm(alarm_time)


# import time#LIBRARY OF PYTHON
# import datetime#LIBRARY OF PYTHON
# #import pygame
# from zoneinfo import ZoneInfo #LIBRARY OF PYTHON

# def set_alarm( alarm_time): #DEFINE SET ALARM FUNCTION ,PASSING IN ALARM TIME AS ARGUMENT/INPUT FROM USER.

#     print(f"Alarm set for {alarm_time}") #ENTERING INTO THE FUNCTION,PRINTING UPDATE TO USER OF ALARM SUCCESFULLY SET.
#     #sound_file = "/"
#     is_running = True # VARIABLE USED TO CONTROL START AND STOP OF ALARM

#     while is_running: #WHILE LOOP THAT DEPENDS ON ISRUNNING VARIABLE, WILL KEEP LOOPING UNTIL ISRUNNING IS FALSE
#         now = datetime.datetime.now(ZoneInfo("America/New_York"))#STORING DATE FOR EST IN NOW VARIABLE, USING IMPORTED LIBRARY DATETIME FUNCTION TO CONVERT THE IMPORTED LIBRARY OF
#         current_time = now.strftime("%I:%M:%S %p")  # 12-hour format
#         print(current_time) #PRINTING THE CURRENT FORMATTED TIME

#         if current_time == alarm_time: # COMPARING IF CURRENT TIME EQUAL THE ALARM TIME SET BY USER
#             print("WAKE UP!!!") # IF YES ALARM PRINT WAKE-UP


#             is_running = False #TURN OFF ALARM

#         time.sleep(1)# TURNS OFF AFTER 1SEC

# if __name__ == '__main__':# ALLOWS APP TO RUN
#         alarm_time = input("Enter the alarm time(HH:MM:SS AM/PM): ") #GETTING INPUT FROM THE USER
#         set_alarm(alarm_time)#CALLING THE FUNCTION AFTER INPUT ACCEPTED PASSING IN THE ALARM TIME
