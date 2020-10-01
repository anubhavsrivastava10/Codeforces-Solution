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
    
import collections
t = ip()
while t:
    t-=1
    n = ip()
    arr = lip()
    arr.sort()
    result = collections.defaultdict(list)
    for i, a in enumerate(arr):
        for j in range(i+1,n):
            if i not in result[a+arr[j]] and j not in result[a+arr[j]]:
                result[a+arr[j]].append(i)
                result[a+arr[j]].append(j)
    z = 0
    for item in result:
        v = len(set(result[item]))//2
        if v>z:
            z = v
    print(z)