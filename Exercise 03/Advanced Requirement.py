"""
Have the user input their name, hometown, and age instead of hard-coding the
values. Try giving both your first and second name when asked for your name.
What happens? How can you handle multiple words in Python? Test the
program by entering a string value for age (e.g., “twenty”). What happens?
How can you prevent this issue?
- After entering my name it stores the string value for example "Danielle Gatan" to string variable name.
- After entering my hometown it stores the string value for example "Bayombong Nueva Vizcaya" to string variable hometown.
- After entering my age either in integer or string it still stores the integer and the string values.
"""
# After entering the 3 variables name, hometown, and age it prints the value of the variable name, hometown, and age.
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
age = int(input("Enter your age: "))

# This is where the information is stored in a dictionary.
profile = {
    "name" : name.title(),
    "hometown" : hometown.title(),
    "age" : age 
    # This is stored as an integer.
}
# This "print" will display the values on different lines.
print(f"Name: {profile['name']}\nHometown: {profile['hometown']}\nAge: {profile['age']}")