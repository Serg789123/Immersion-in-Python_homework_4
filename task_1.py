# Напишите функцию для транспонирования матрицы
def trans(data):
    t_matrix = [[0 for j in range(len(data))] for i in range(len(data[0]))] # создаём матрицу с незаполннеными значениями

    for i in range(len(data)):
        for j in range(len(data[0])):
            t_matrix[j][i] = matrix[i][j]
    return t_matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
trans_matrix = trans(matrix)
print(f'{matrix=}\n{trans_matrix=}')

