#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Outer interation
    for row in matrix:
        # Inner iteration
        for num in row:
            print("{:d}".format(num), end=" ")
        print()
