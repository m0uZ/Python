# Напишите функцию для транспонирования матрицы.

def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    temp_matrix = [[0] * rows for _ in range(columns)]
    for i in range(rows):
        for j in range(columns):
            temp_matrix[j][i] = matrix[i][j]
    return temp_matrix


some_matrix1 = [[1, 2], [3, 4], [5, 6], [7, 8]]
some_matrix2 = transpose_matrix(some_matrix1)

print(some_matrix2)
