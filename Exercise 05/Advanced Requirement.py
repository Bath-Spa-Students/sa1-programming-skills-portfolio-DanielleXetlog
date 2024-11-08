"""
Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.
"""

"""
Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.
"""

# The dictionary shows the numbers of days in each month.
# Also note that Febuary is has 29 days (Leap years is not included for simplicity).
month_and_days = {
    1: 31, # Jan
    2: 28, # Feb
    3: 31, # Mar
    4: 30, # Apr
    5: 31, # May
    6: 30, # Jun
    7: 31, # Jul
    8: 31, # Aug
    9: 30, # Sep
    10: 31, # Oct
    11: 30, # Nov
    12: 31, # Dec
}

# This ask the user to type in the month number. 
# It also converts to an integer to match the dictionary keys.
month_num = int(input("Enter the month number (1-12): "))

# If the user typed below 1 or more than 12 it will print out an error message.
if month_num < 1 or month_num > 12:
    print("Please enter a valid month number between 1 and 12.")
# If the user picked Febuary it will ask the user if it is a leap year and be given a choice of yes or no.
elif month_num == 2:
    leap_year = input("Is it a leap year? (yes or no): ").strip().lower()
    if leap_year == "yes":
        month_and_days[2] = 29 
    print(f"There are {month_and_days[month_num]} days in month {month_num}.")
# For the other valid months it will print out the number of days.
else:
    print(f"There are {month_and_days[month_num]} days in month {month_num}.")

# If statement is used to check if the condition is true.
# Elif statement is used to check if the condition is false and the program goes to the elif to check another condition.
# Else statement is used to run the code if there's no other conditions that are true.
