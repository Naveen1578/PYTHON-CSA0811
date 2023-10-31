def sum_boundary_elements(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    boundary_sum = 0
    for i in range(cols):
        boundary_sum += matrix[0][i]
    if rows > 1:
        for i in range(cols):
            boundary_sum += matrix[rows - 1][i]
    if cols > 1:
        for i in range(1, rows - 1):
            boundary_sum += matrix[i][0]
        for i in range(1, rows - 1):
            boundary_sum += matrix[i][cols - 1]

    return boundary_sum

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = sum_boundary_elements(matrix)
print("Sum of boundary elements:", result)
