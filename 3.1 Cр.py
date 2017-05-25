import math
x=int(input("Введите X: "))
s=0
for i in range(1,9):
    if i!=3:
        k=((math.fabs(7-x))**i)/((i-3)**5)
    p=1
    for n in range(i,17):
        if n!=12:
            m=((n**3)-8)/(n-12)
        p=p*m;
    s=s+k+p
W=s
print(W)
