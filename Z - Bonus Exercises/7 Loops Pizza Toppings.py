"""
Write a loop that prompts the user to enter a series of pizza toppings until they enter a
'quit' value. As they enter each topping,
Print a message saying you’ll add that topping to their pizza.
"""
# Empty list to put the pizza stoppings
toppings = []
# Creates an infinite loop to take the users toppings.
while True:
    topping = input("Please enter a pizza topping('quit' to finish): ")
    # Checks the user wants to quit.
    if topping.lower() == 'quit':
        # Exits the loop
        break
    # Add entered toppings to the list.
    toppings.append(topping)
    # Tells the user that the topping are being added.
    print(f"Please wait. Adding {topping} to your pizza.")
# Displays all the list of topping that the user chose.
print("Your pizza toppings are:")
for topping in toppings:
    # Print each toppings that were in the list.
    print(f"- {topping}")