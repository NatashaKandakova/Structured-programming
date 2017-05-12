s=input('Введите строку с буквой, повторяющейся двжды - ')

for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
         k=s[i]
print('Повторяющаяся буква   ',k)
