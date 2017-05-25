X=[int(input("Элемент массива X ")) for i in range(10)]
print()
Y=[int(input("Элемент массива Y ")) for i in range(10)]
print('Исходный массив X: ',X)
print('Исходный массив Y: ',Y)
S=[]
for i in range(10):
    for j in range (10):
        if X[i]==Y[j]:
            k=X[i]
            S.append(k)
print('Получившийся массив :',S)
  
