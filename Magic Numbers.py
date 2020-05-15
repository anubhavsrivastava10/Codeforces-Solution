x = input()
if x[0]!='1':
    print('NO')
else:
    c=0
    k=9
    for i in range(1,len(x)):
        if x[i]=='4':
            c+=1
            if c>2:
                k=1
                break
        if x[i]=='1':
            c=0
        if x[i]!='1' and x[i]!='4':
            k=1
            break
    if k!=1:
        print('YES')
    else:
        print('NO')