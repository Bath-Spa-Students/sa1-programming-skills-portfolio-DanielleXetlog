"""
Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console
in each case.
* Write a loop that counts up from 0 to 50 in increments of 1.
* Write a loop that counts down from 50 to 0 in decrements of 1.
* Write a loop that counts up from 30 to 50 in increments of 1.
* Write a loop that counts down from 50 to 10 in decrements of 2.
* Write a loop that counts up from 100 to 200 in increments of 5.  
"""
# Generates list of numbers from 0 to 50 in increments of 1.
list1 = [num for num in range(0,51,1)]
# Prints the list.
print(f'\n{list1}')
# Generates list of numbers down to 50 to 0 in decrement of 1.
list2 = [num for num in range(50,-1,-1)]
# Prints the list.
print(f'\n{list2}')
# Generates list of numbers up to 30 to 50 in decrement of 1.
list3 = [num for num in range(30,51,1)]
# Prints the list.
print(f'\n{list3}')
# Generates list of numbers down to 50 to 10 in decrement of 2.
list4 = [num for num in range(50,9,-2)]
# Prints the list.
print(f'\n{list4}')
# Generates list of numbers up to 100 to 200 in decrement of 5.
list5 = [num for num in range(100,201,5)]
# Prints the list.
print(f'\n{list5}')
