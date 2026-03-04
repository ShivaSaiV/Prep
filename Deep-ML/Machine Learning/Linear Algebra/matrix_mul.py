import numpy as np

def matrixmul(a, b):
	if len(a[0]) != len(b):
		return -1
	return np.matmul(a, b)


print(matrixmul([[1,2,3],[2,3,4],[5,6,7]],[[3,2,1],[4,3,2],[5,4,3]]))