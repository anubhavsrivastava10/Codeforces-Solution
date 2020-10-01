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
    lst = lip()
    a = min(arr)
    b = min(lst)
    count = 0
    for i in range(n):
        count+= max(arr[i]-a,lst[i]-b)
    print(count)