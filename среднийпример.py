import math
a= float (input('a= '))
t= float (input('t= '))
y= float (input('y= '))
D=(7.8*(a**2)+3.52*t)/(math.log(a+2*y)+math.exp(y))
print (D)
