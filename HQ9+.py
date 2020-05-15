x = input()
c=1
for i in x:
    if i=='H' or i=='Q' or i=='9':
        c=0
        print('YES')
        break
if c==1:
    print('NO')