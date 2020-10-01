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


n,m = mip()
if n==1:
    print(1)
elif m-1<n-m:
    print(m+1)
else:
    print(m-1)
