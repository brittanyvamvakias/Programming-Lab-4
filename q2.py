# File: q2.py
# Author: Brittany Vamvakias
# Date: 02/20/2020
# Section: 501
# E-mail: brittvam@tamu.edu
# Description: This code takes the dimensions of two different matrices, A and B, and checks if any of the four dimensions is greater that 10 and if the two matrices can be multiplied. A and B are multiplied, giving a result of C. Matrix C is then transposed.

print("***************************************************************")
quit = False
while quit == False:
    row_A, col_A = input("Enter matrix A rows and columns: ").split()
    row_A, col_A = int(row_A), int(col_A)

    row_B, col_B = input("Enter matrix B rows and columns: ").split()
    row_B, col_B = int(row_B), int(col_B)

    if (row_A or col_A or row_B or col_B) > 10:
        print("Invalid input. Too many rows and/or columns. I quit!")
        quit == True
        break
    elif col_A != row_B:
        print("Matrices can't be multiplied. The columns of matrix A must be equal to the rows in matrix B. I quit!")
        quit == True
        break
    else:
        pass

    # this splits every component individually
    A = input("Enter matrix A: ").split()
    # this splits the components into each row
    A = [A[i:i + col_A] for i in range(0, len(A), col_A)]

    B = input("Enter matrix B: ").split()
    B = [B[i:i + col_B] for i in range(0, len(B), col_B)]

    print(f"Matrix A:")
    print(*A, sep="\n")
    print(f"Matrix B:")
    print(*B, sep="\n")

    # C will have row_A rows and col_B columns
    C = [[0 for row in range(len(B[0]))] for col in range(len(A))]

    # multiplication of A and B to get C
    for rows_A in range(len(A)):  # iterates through rows of A
            for cols_A in range(len(A[0])):
                for cols_B in range(len(B[0])):  # iterates through columns of B
                    for rows_B in range(len(B)):  # iterates through rows of B
                        C[rows_A][cols_B] += int(A[rows_A][cols_A]) * int(B[rows_B][cols_B])

    print(f"Matrix A times matrix B is equal to matrix C: {C}")

    # transpose of C
    # transpose swaps the rows and columns of a matrix
    transposeC = [[0 for x in range(len(C))] for y in range(len(C[0]))]
    for rows_C in range(len(C[0])):
        for cols_C in range(len(C)):
            transposeC[rows_C][cols_C] = C[cols_C][rows_C]

    print(f"The transpose of matrix C is {transposeC}")
    quit = True


print("***************************************************************")
