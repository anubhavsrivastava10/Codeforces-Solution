t = int(input())
while t:
    t-=1
    x,y,n = map(int,input().split())
    z = n%x
    if z==y:
        print(n)
    elif z>y:
        print(n-(z-y))
    else:
        print(n-z-(x-y))