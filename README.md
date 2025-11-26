# Alarm Clock ⏰  
A simple Python alarm clock that displays time in **Eastern Time (EST/EDT)** and uses a clean **12-hour AM/PM format**.  
This project was created for learning purposes and includes internal documentation to help understand how the code works.

---

## 🚀 Features

- Displays current time in **Eastern Time** using Python’s `zoneinfo`
- Uses **12-hour format** with AM/PM (easier to read than 24-hour format)
- Checks the time every second until it reaches the alarm time
- Simple terminal-based interface
- Beginner-friendly Python code with helpful comments

---

## 🧠 How It Works

The program:
1. Asks the user to enter an alarm time (example: `07:30:00 AM`)
2. Retrieves the **current EST/EDT time** using:
   ```python
   datetime.datetime.now(ZoneInfo("America/New_York"))
3. Formats the time as:

%I:%M:%S %p


Example: 03:15:45 PM

4. Compares the current time to the alarm time every second

5. Prints WAKE UP!!! when the time matches

📦 Requirements

This project uses only built-in Python modules except for one:

Python 3.9+

tzdata (required on Windows for time zone support)

Install tzdata if needed:

pip install tzdata

▶️ Running the Program

Run the script from your terminal:

python alarm_clock.py


Then enter your alarm time:

Enter the alarm time (HH:MM:SS AM/PM): 07:30:00 AM


The program will print the time every second until the alarm triggers.
