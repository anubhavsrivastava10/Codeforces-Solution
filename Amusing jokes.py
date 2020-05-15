a = input()
b = input()
c = input()
x =  a+b

if len(x) == len(c):
    x = sorted(x)
    c = sorted(c)
    for i in range(len(x)):
        if x[i]==c[i]:
            if i==len(x)-1:
                print('YES')
        else:
            print('NO')
            break
else:
    print('NO')