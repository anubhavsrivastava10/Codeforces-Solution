def lp():
    return list(map(int,input().split()))
def ip():
    return int(input())

t = int(input())
while t:
    t-=1
    lst = lp()
    lst.sort()
    x = lst[0]
    y = lst[1]
    z = lst[2]
    a = 1
    b = x
    c = y
    if z==max(b,c):
        print('YES')
        print(a,b,c)
    else:
        print('NO')