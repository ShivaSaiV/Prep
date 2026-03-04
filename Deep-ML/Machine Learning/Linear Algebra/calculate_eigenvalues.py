import numpy as np

def calculate_eigenvalues(matrix):
	a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]

	b_q = a + d
	c_q = a * d - b * c 

	val1 = (b_q + np.sqrt(b_q**2 - 4*c_q)) / 2
	val2 = (b_q - np.sqrt(b_q**2 - 4*c_q)) / 2


		
	return [val1, val2]


print(calculate_eigenvalues([[2, 1], [1, 2]]))