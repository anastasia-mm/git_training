def ex10(matrix):
    mas = []
    for j in range(len(matrix[0])):
        s = 0
        for i in range(len(matrix)):
            s += matrix[i][j]
        mas.append(s)
    matrix.append(mas)
    for i in range(len(matrix)):
        matrix[i].append(0)
    for k in range(len(matrix[0])-2):
        for i in range(len(matrix[0])-2):
            if matrix[-1][i] > matrix[-1][i+1]:
                for j in range(len(matrix)):
                    matrix[j][-1] = matrix[j][i]
                    matrix[j][i] = matrix[j][i+1]
                    matrix[j][i+1] = matrix[j][-1]
    matrix.pop(-1)
    for i in range(len(matrix)):
        matrix[i].pop(-1)
    return matrix


def vivod(matrix):
    for line in matrix:
        for column in line:
            print('%4d' % column, end=' ')
        print()
    return ''
