N=int(input("Введите N: "))
i=1
while i<=N:
    k=i
    s=0
    while k>0:
        s=s+k%10
        k=int(k/10)
    if ((i%5!=0)and(i%3==0)and((s%5!=0)and(s%3==0))):
        print(i)
    i=i+1
