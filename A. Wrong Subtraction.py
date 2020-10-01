def iip():
    return int(input())

def sip():
    return input()

def mip():
    return map(int,input().split())

def lip():
    return list(map(int,input().split()))

n,k = mip()
for i in range(k):
    if n%10==0:
        n = n//10
    else:
        n-=1
print(n)