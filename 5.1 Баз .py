a=[int(input("Элемент массива ")) for i in range(9)]
print('Исходный массив: ',a)
mn = min(a)
mx = max(a)
imn = a.index(mn)
imx = a.index(mx)
a[imn],a[imx] = a[imx],a[imn]
print('Изменённый массив: ',a)

