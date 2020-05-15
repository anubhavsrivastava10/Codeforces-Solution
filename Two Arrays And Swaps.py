for i in range(int(input())):
    n,k = map(int,input().split())
    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())))[::-1]
    for i in range(k):
        if a[i]<b[i]:
            a[i],b[i]=b[i],a[i]
    print(sum(a))