def iip():
    return int(input())

def sip():
    return input()

def mip():
    return map(int,input().split())

def lip():
    return list(map(int,input().split()))

n,k = mip()
arr = lip()
val = arr[k-1]
count = 0
for i in range(n):
    if arr[i]>=val and arr[i]!=0:
        count+=1
print(count)