def iip():
    return int(input())

def sip():
    return input()

def mip():
    return map(int,input().split())

def lip():
    return list(map(int,input().split()))

t = iip()
while t:
    t-=1
    n,a,b = mip()
    arr = lip()
    lst = lip()
    arr.sort()
    lst.sort()
    if arr[-1]>lst[-1]:
        print('YES')
    else:
        print('NO')