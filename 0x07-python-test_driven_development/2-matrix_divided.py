#!/usr/bin/python3
""" A module that defines matrix_divided method"""


def matrix_divided(matrix, div):
    """ divides each element of the matrix by div

    Args:
    matrix: list of lists containing int and float
    div: number to divide matrix by

    Returns:
    list: lists of lists representing the matrix

    Raises:
    TypeError: if matrix is not list of lists of integers or floats
    TypeError: if matrix row are not the same size
    TypeError: if div is not an int or float
    ZeroDivisionError: if div is 0
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div === 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        "of integers/floats")

      for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")

