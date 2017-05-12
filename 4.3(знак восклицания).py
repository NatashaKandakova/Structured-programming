s=input('Введите строку с восклицательным знаком - ')

for i in range(len(s)):
    if s[i]=='!':
        s=s[0:i]+str(i)+s[i+1:]
print('Ваша строка   ',s)
