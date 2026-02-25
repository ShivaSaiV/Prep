import numpy as np

"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
"""

def cosine_similarity(v1, v2):

    if v1.shape[0] != v2.shape[0]:
        return -1

    numerator = np.dot(v1, v2)
    
    v1_mag = np.linalg.norm(v1)
    v2_mag = np.linalg.norm(v2)


    return numerator / (v1_mag * v2_mag)
	



v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])
print((cosine_similarity(v1, v2)))
