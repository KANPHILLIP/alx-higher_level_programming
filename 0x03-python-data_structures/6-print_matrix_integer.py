#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for num in row:
                print("{:d}".format(num), end=" " if num != [row] else "")
            print()
