#x=1+A+A2++AN   y=1-A+A2-A3+ +(-1)AN
A=float (input('Введите A: '))
N=int (input('Введите N: '))
x=1
y=1
for i in range (N+1):
    x=x+A*i
print("x=", x)
for i in range (N+1):
    if i%2==0: y=y+A*i
    else:y=y-A*i
print("y=", y)
    