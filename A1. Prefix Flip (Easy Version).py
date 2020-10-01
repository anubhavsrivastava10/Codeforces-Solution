t = int(input())
while t:
    t-=1
    n = int(input())
    a = input()
    b = input()
    lst = []
    for i in range(n):
        if a[i]!=b[i]:
            if i>0:
                lst.append(i+1)
            lst.append(1)
            if i>0:
                lst.append(i+1)
    print(len(lst),end=' ')
    print(*lst)