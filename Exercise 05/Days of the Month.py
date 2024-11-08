"""
Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.
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

# If the user typed less than 1 it will print out to say put a valid number between 1-12.
if month_num < 1:
    print("Please enter a valid month number between 1 to 12.")
# If the user typed more than 12 it will print out to say put a valid number between 1-12.
elif month_num > 12:
    print("Please enter a valid month number between 1 to 12.")
# If the user typed the valid numbers between 1-12, it will print out how many days is in that month.
else: 
    print(f"There are {month_and_days[month_num]} days in month {month_num}.")
# If statement is used to check if the condition is true.
# Elif statement is used to check if the condition is false and the program goes to the elif to check another condition.
# Else statement is used to run the code if theres no other conditions that are true.