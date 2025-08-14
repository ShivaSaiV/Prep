import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
    if len(a[0]) != len(b):
        return -1
    dot_prod = []
    for row in a:
        dot_prod.append(np.dot(row, b))

    return dot_prod
