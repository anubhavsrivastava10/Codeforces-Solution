x = input()
f=0
for i in x:
    if i=='4' or i=='7':
        f+=1
if f==4 or f==7:
    print('YES')
else:
    print('NO')