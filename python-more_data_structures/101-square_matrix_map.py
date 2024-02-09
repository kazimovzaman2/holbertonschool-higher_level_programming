#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    def square_row(row):
        return list(map(square_element, row))

    def square_element(x):
        return x ** 2

    return list(map(square_row, matrix))
