"""
In this exercise, you’ll create a simple program that asks the user a question,
evaluates their answer, and provides feedback.
Steps:
1. Write a program that asks the user “What is the capital of France?” and
waits for their response.
2. If the user’s answer is correct (i.e., “Paris”), the program should print a
message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the
answer is wrong.
"""

# The user will be asked "What is the capital of France?"
# input is used to capture the users answer the question.
question = input("What is the capital of France? ")
# This will access the user's answer and give feedback onces the user entered the answer.
# strip() is used to remove any spaces and convert the text to lowercase.
# if is used to check if the processed answer is "paris" it basically just checks whether the answer is right or wrong.
# else is used to print wrong if the answer isnt the right answer.
if question.strip().lower()== "paris": 
    print("Correct!")
else:
    print("Wrong! The correct answer is Paris")