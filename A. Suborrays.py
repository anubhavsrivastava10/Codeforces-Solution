def ip():
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

t = ip()
while t:
    t -= 1
    n = ip()
    lst = []
    for i in range(1,n+1):
        lst.append(i)
    print(*lst)
