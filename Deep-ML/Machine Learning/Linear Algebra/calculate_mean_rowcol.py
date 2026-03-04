def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	matrix_t = [list(row) for row in zip(*matrix)]
	if mode == 'column':
		for i in range(len(matrix_t)):
			total = sum(matrix_t[i])
			mean = total / len(matrix_t[0])
			means.append(mean)
	else:
		for i in range(len(matrix)):
			total = sum(matrix[i])
			mean = total / len(matrix[0])
			means.append(mean)
	return means


print(calculate_matrix_mean([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'column'))