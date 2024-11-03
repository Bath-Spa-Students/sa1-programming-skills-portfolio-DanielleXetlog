"""
Instructions: In this exercise, you’ll create a program that stores and prints your name, home-
town, and age to the console using a Python dictionary.

Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a
dictionary.
2. Print the values on separate lines using a single print() statement.
3. Use variables with appropriate data types for each piece of information.
"""
    

# Using the Dictionary variable "profile" with key-value pairs.
# The key called "name" holds the value of "Danielle Gabrielle C. Gatan"
profile ={
    "name" : "Danielle Gabrielle C. Gatan",
# The string "Bayombong Nueva Vizcaya" is assigned to a key value named "hometown"
    "hometown" : "Bayombong Nueva Vizcaya",
# The integer "17" is assigned to a key value named "age"
    "age" : int(17)
}
# Looking at the name "print" means it prints the values that are stored in the dictionary on different lines.
# The "f-strings" is for the formatted output
# The "\n" prints a new line after each print statement
print(f"Name: {profile['name']}\nHomework: {profile['hometown']} \nAge: {profile ['age']}")