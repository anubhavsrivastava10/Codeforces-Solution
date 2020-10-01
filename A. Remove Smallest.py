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
    t-=1
    n = ip()
    arr = lip()
    arr.sort()
    flag = 0
    for i in range(1,n):
        if arr[i]-arr[i-1]>1:
            flag = 1
            break
    if flag==1:
        print('NO')
    else:
        print('YES')