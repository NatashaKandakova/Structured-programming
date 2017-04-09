import math
a= float (input('a='))
b= float (input('b='))
c= float (input('c='))
D=b**2-(4*a*c)
if (D>0):
    x2=(-b-math.sqrt(D))/(2*a)
    x1=(-b+math.sqrt(D))/(2*a)
print(D)
print(x1)
print(x2)

