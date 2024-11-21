"""
Write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam". 
"""
# List of names to search.
people = ["Jake","Zac","Ian","Ron","Sam","Dave"]
# Target name of the person we are searching.
target_person = "Sam"
# Indicates if target person is found.
found = False
# Searches again through the people to find the target person.
for person in people:
    if person == target_person:
        # Set indicator and stop searching if the person is found.
        found = True
        break
# Prints if the target person is found.
if found:
    print(f"{target_person} is on the list.")
# Prints if the target person is not found.
else:
    print(f"{target_person} is not on the list.")
