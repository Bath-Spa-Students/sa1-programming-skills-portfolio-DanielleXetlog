"""
Write a program that tests if a value is even or odd. Follow the instructions outlined below:

### Instructions:
* The program should ask the user for a number from within the main function.
* The entered number should be passed to a function that determines if the value is even or odd.
* The function should return a message indicating whether the number is even or odd.
* The message returned by the function should be printed from within the main function. 
"""

# A function to check if the number is even or odd.
def even_or_odd(num):
    # Checks if the number is even.
    if num % 2 == 0:
        return f"The number {num} is even."
    # Checks if the number is odd.
    else:
        return f"The number {num} is odd."
    
    # Defines the main function
def main():
    # Input of the user to enter a number.
    user_entry = int(input("Enter a number here: "))
    # Checks if the number is even or odd.
    ans = even_or_odd(user_entry)
    # Displays the answer
    print(ans)
# Runs the main function if the code is executed directly.
if __name__ == "__main__":
    main()