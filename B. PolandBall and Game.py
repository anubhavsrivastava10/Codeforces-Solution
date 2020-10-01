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
lst=[]
arr = []
for i in range(n):
    s = sip()
    lst.append(s)
for i in range(m):
    s = sip()
    arr.append(s)
if n>m:
    print('YES')
elif m>n:
    print('NO')
else:
    lst = set(lst)
    arr = set(arr)
    arr = set(arr.intersection(lst))
    if len(arr)%2==0:
        print("NO")
    else:
        print("YES")