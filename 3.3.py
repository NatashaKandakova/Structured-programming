import math
N=int(input("Введите N: "))
x=int(input("Введите x: "))
s=0
k=1
for i in range(1,N):
    if k%2!=0:
        s=s+(math.cos(k*x)/(k**2))
    k=k+1
    i=i+1
print(s)
