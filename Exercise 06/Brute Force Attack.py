"""
Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
3. Output an appropriate message when the correct password is entered.
"""
# This is the correct password to be typed by the user.
right_pass = "12345"
# I used a while loop so the user can have another try until the password is correct.
while True:
    # This will ask the user to type the password.
    typed_pass = input("Please enter the password: ")
    # If will check if the correct answer is the same.
    if typed_pass == right_pass:
        print("Entry sucess.")
        break 
    elif typed_pass != right_pass:
        # This will show if the answer is wrong and get a chance again.
        print("Invalid password. Please try again.")
    else:
        # This else block will skip due to the elif condition.
        print("System malfunction.")
        
# If statement is used to check if the condition is true.
# Elif statement is used to check if the condition is false and the program goes to the elif to check another condition.
# Else statement is used to run the code if theres no other conditions that are true.
# Break condition is used to exit loops.
    