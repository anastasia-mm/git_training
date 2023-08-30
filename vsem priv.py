import random
n = 3
m = 4
matrix = [[random.randint(1, 10) for i in range(m)] for j in range(n)]
print(matrix)
for line in matrix:
    for element in line:
        print("%4d" % element, end=' ')
    print()
print()
print('\n'.join([' '.join('{:{width}}'.format(element, width=4) for element in line) for line in matrix]))
