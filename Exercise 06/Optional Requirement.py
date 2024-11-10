"""
Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.
"""
# This is the correct password to be typed by the user.
right_pass = "12345"

attempts_left = 5
# I used a while loop so the user can have another try until the password is correct.
while attempts_left > 0:
    # This will ask the user to type the password.
    typed_pass = input("Please enter the password: ")
    # If will check if the correct answer is the same.
    if typed_pass == right_pass:
        print("Entry success.")
        break
    elif typed_pass != right_pass:
        attempts_left -= 1
        if attempts_left > 0:
            # This will show if the user got the password wrong.
            print(f"Invalid password. You have {attempts_left} attempts left. Please try again.")
        else:
            # This will show if the user used all of the attempts.
            print("Invalid password. You have no more attempts left. The authorothies have been notified.")
            break
    else: 
        # This else block will skip due to the elif condition.
        print("System malfunction.")
# If statement is used to check if the condition is true.
# Elif statement is used to check if the condition is false and the program goes to the elif to check another condition.
# Else statement is used to run the code if theres no other conditions that are true.
# Break condition is used to exit loops.
    