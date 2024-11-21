"""
Imagine an alien was just shot down in a game. Create a variable called alien_color and
assign it a value of 'green', 'yellow', or 'red'.
•Write an if statement to test whether the alien’s color is green. If it is, print a message
that the player just earned 5 points.
•Write one version of this program that passes the if test and another that fails. (The
version that fails will have no output.)
"""
# Puts the alien's color to green
alien_color = 'green'
# If checks if the alien's color is the same.
if alien_color == 'green':
    # If its true this will display.
    print("The player just recieved 5 points.")
# Made the alien color to yellow.
alien_color = 'yellow'
# Checks again if the alien color is green.
if alien_color == 'green':
    # This will block and not contiue since the alien color is now different.
    print("The player just recieved 5 points.")
    
