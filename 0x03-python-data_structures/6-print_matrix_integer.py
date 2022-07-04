#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for num in list:
            if num in list[:-1]:
                print('{:d}'.format(num), end=' ')
            else:
                print('{:d}'.format(num), end='')
        print('')
