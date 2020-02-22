# File: q1.py
# Author: Brittany Vamvakias
# Date: 02/20/2020
# Section: 501
# E-mail: brittvam@tamu.edu
# Description: This code takes an input from the user for the length of a list, between 2 and 10, and then asks for the entry at each index of this new list. The code checks if each entry is a positive number before moving on. It then asks for a desired value and checks to see if any of the indexes add up to that desire value. If not, it just sums all the values.

print("******************************* Section A ********************************")

valid = False

while valid == False:
    length1 = int(input("Enter the length: "))
    if (length1 > 2) and (length1 < 10):
        print(f"Variable length1 is {length1}")
        valid = True
    else:
        print("Invalid length1 input, try again")
        continue  # repeats the loop until the user inputs a valid length1

print("******************************* Section B ********************************")

list_A = []
valid = False

for index in range(length1):
    while valid == False:
        entry = int(input(f"Enter the entry at index number {index}: "))
        if entry > 0:
            list_A.append(entry)
            break  # breaks into the for loop
        else:
            print(f"Invalid entry at index number {index}")
            print()
            continue  # restarts the while loop with the same index

print("******************************* Section C ********************************")

target1 = int(input("Enter target value: "))

valid = False
complete = False
sum = 0

while valid == False:
    for value in range(len(list_A)):
        if complete == False:
            for n in range(1, len(list_A)):
                if list_A[value] + list_A[n] == target1:
                    print(f"The entries {list_A[value]},{list_A[n]} at index {value},{n} sum to {target1}")
                    complete = True
                    break  # breaks into the outer for loop
                else:
                    continue  # continues with the inner for loop

        elif complete == True:
            valid = True
            break
        else:
            print("No such entries were found.")
            for x in range(len(list_A)):
                sum += list_A[x]
            print(f"The sum is {sum}")
            valid = True
            break


print("***************************************************************")

