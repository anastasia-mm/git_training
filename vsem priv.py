import random
n = 3
m = 4
matrix = [[random.randint(1, 10) for i in range(m)] for j in range(n)]
print(matrix)
for line in matrix:
    for element in line:
        break
        print("%4d" % element, end=' ')
    print()
print()

# функция принимает матрицу, возвращает максимальный элемент среди минимальных элементов столбцов
def ex_9 (matrix):
    min_column = []
    for i in range(m):
        column = []
        for j in range(n):
            column.append(matrix[j][i])
        min_column.append(min(column))
    return max(min_column)