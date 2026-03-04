import numpy as np

def inverse_2x2(matrix):
	"""
	Calculate the inverse of a 2x2 matrix.
	
	Args:
		matrix: A 2x2 matrix represented as [[a, b], [c, d]]
	
	Returns:
		The inverse matrix as a 2x2 list, or None if the matrix is singular
		(i.e., determinant equals zero)
	"""
	a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]

	det = a * d - b * c 

	if det == 0:
		return None
	
	a_inv = np.array([[d, -1 * b], [-1 * c, a]])

	a_inv = a_inv * (1/det)

	return a_inv



print(inverse_2x2([[4, 7], [2, 6]]))