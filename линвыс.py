import math
a= float (input('a='))
b= float (input('b='))
c= float (input('c='))
D=b**2-(4*a*c)
print('D=',D)
if (D>0):
    x2=(-b-math.sqrt(D))/(2*a)
    x1=(-b+math.sqrt(D))/(2*a)
    print('x1=',x1)
    print('x2=',x2)
else : print('Дискриминант меньше нуля')




