# File: q3.py
# Author: Brittany Vamvakias
# Date: 02/20/2020
# Section: 501
# E-mail: brittvam@tamu.edu
# Description: This code takes an input for a number from the user and splits each integer into its own index in a list. One is then added to the number, and each index of the list is updated to match the new value. If the new number requires an additional digit, the code adds to the list and updates all the values.

print("***************************************************************")

list = input("Enter single digits seperated by one space: ").split()

for index in range(len(list)):  # turns the strings to integers
    list[index] = int(list[index])

# starts the loop at the -1 index
for num in range(-1, -len(list) - 1, -1):
    # this catches if the -1 index is at 9 and handles the carry over
    if list[num] == 9:
        list[num] = 0
        list[num - 1] += 1
        # this keeps the code from catching another 9 in the list
        if list[num - 1] != 10:
            break
        else:
            pass
    # this catches if the 0 index is equal to 10, and if a new index needs to be added at the beginning
    elif list[-len(list)] == 10:
        list[-len(list)] = 0
        list.insert(0, 1)
    # this catches if more needs to be carried over
    elif list[num] == 10:
        list[num] = 0
        list[num - 1] += 1
    # this runs if the -1 index is less than 9
    else:
        list[num] += 1
        break


print(list)

print("***************************************************************")
