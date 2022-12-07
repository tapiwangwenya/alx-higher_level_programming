#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (new_matrix)
