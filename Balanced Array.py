for _ in range(int(input())):
    n = int(input())
    x = n//2
    lst=[]
    if x%2==0 and x>=2:
        print('YES')
        for i in range(1,(2*x)+1):
            if i%2==0:
                lst.append(i)
        k = sum(lst)
        for i in range(1,2*x-1):
            if i%2!=0:
                lst.append(i)
        p = sum(lst)
        z = p-k
        p = k-z
        lst.append(p)
        print(*lst)
    else:
        print('NO')