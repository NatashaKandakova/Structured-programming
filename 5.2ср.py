#сортировка последнего столбца
from random import random
N=5
M=4
matrix = []
print('исходная матрица:')
for i in range(N):
    a = [0] * M
    for j in range(M):
        a[j] = int(random()*10)
        print('%3d' % a[j],end='')
    matrix.append(a)
    print()

matrix.sort(key=lambda i:i[3], reverse=True)
print('сортировка по последнему столбцу:')
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
         print('%3d' % matrix[i][j], end='')
    print()
