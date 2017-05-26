n=3
matrix = []
print('заполненный массив:')
for i in range(n):
    a = [0] * n
    for j in range(n):
        a[j] = (n - 2 * i) * (n - 2 * i - 1) + (i - j) * (
        (i <= j) * (4 * (i + j - n) + 2) * (2 * (i + j <= n - 1) - 1) + 1 + 4 * (i + j <= n - 1) * (n - i - j - 1)) + 1
        print('%3d' % a[j],end='')
    matrix.append(a)
    print()
