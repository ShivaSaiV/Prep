def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    result = []
    for row in matrix:
        n_row = [scalar * val for val in row]
        result.append(n_row)
            
    return result


print(scalar_multiply([[1,2],[3,4]], 2))