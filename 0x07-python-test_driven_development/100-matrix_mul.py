#!/usr/bin/python3
"""function that multiplies 2 matrices"""

def validate_matrix(matrix, name):
    if not isinstance(matrix, list):
        raise TypeError("{} must be a list".format(name))
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("{} must be a list of lists".format(name))
    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise ValueError("{} can't be empty".format(name))
    if any(not isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("{} should contain only integers or floats".format(name))
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("each row of {} must be of the same size".format(name))

def matrix_mul(m_a, m_b):
    validate_matrix(m_a, "m_a")
    validate_matrix(m_b, "m_b")

    rows_a = len(m_a)
    cols_a = len(m_a[0])
    rows_b = len(m_b)
    cols_b = len(m_b[0])

    if cols_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
