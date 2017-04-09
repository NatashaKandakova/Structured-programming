import math
t=4.1
p= float (input('p='))
k=math.sqrt(p*t)
x=p*t**2+math.sqrt(k)
y=(math.tan(x**2)**3)+k*t
print(k)
print(x)
print(y)
