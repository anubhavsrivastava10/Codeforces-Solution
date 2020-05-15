for _ in range(int(input())):
    x = input()
    s=''
    if len(x)<=10:
        print(x)
    else:
        s+=x[0]
        s+=str(len(x)-2)
        s+=x[-1]
        print(s)