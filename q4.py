# File: q4.py
# Author: Brittany Vamvakias
# Date: 02/20/2020
# Section: 501
# E-mail: brittvam@tamu.edu
# Description: This code asks for the starting and ending value for a Fibonacci seqeunce. The sequence is then created until the final value is greater than or equal to the ending value. The sequence is then printed, starting from the starting value.

valid = True
print("***************************************************************")

while valid == True:
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    if (start or end) < 0:  # checks if the input is positive
        print("Invalid input. I quit!")
        break
    elif start > end:  # checks/adjusts the start and end to be in order
        start, end = end, start
    else:
        pass

    n1 = 0
    n2 = 1
    fib = [n1, n2]
    nth = 0

# this creates a list of the fibonacci sequence until the ending
    while nth <= end:
        nth = n1 + n2
        fib.append(nth)
        n1 = n2
        n2 = nth

# checks if the starting number is in the sequence
    if fib.count(start) > 0:
        starting_index = fib.index(start)
# if not, finds the first value greater than the starting number
    else:
        for value in range(len(fib)):
            if fib[value] > start:
                starting_index = value
                break
            else:
                continue

    if fib[-1] == end:
        final = fib[starting_index:len(fib)]
        print(f"The {len(final)} Fibbonacci numbers between {start} and {end} are:")
        for each in range(len(final)):
            print(final[each], end=" ")
        valid = False

    else:
        final = fib[starting_index:len(fib) - 1]
        print(f"The {len(final)} Fibbonacci numbers between {start} and {end} are:")
        for each in range(len(final)):
            print(final[each], end=" ")
        valid = False

print()

print("***************************************************************")
