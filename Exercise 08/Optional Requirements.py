"""
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.
"""
# List of the people.
people = ["Jake","Zac","Ian","Ron","Sam","Dave"]
# User will be asked to put the name they want to search for.
search_person = input("Enter the name you want to look for: ")
# Initialize a indicator to see if the person is found.
found = False
# Searches again through the people to find the target person.
for person in people:
    # Checks if the person is in the list.
    if person == search_person:
        found = True
        break
    
if found:
    # Prints if the target person is found.
    print(f"{search_person} is in the list.")
else: 
    # Prints if the target person is not found.
    print(f"{search_person} is not in the list.")