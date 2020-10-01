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
        
n,m = mip()
arr = matip(n,m)
val = -1
for i in range(n):
    l = min(arr[i])
    if l>val:
        val = l
print(val)