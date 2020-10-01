def iip():
    return int(input())

def sip():
    return input()

def mip():
    return map(int,input().split())

def lip():
    return list(map(int,input().split()))

def matip(n,m):
    lst=[]
    for i in range(n):
        arr = lip()
        lst.append(arr)
    return lst

t = iip()
while t:
    t-=1
    a,b = mip()
    if 2*a<=b:
        print(a,2*a)
    else:
        print(-1,-1)