def iip():
    return int(input())

def sip():
    return input()

def mip():
    return map(int,input().split())

def lip():
    return list(map(int,input().split()))

t = iip()
count = 0
while t:
    t-=1
    p,q = map(int,input().split())
    if q-p>=2:
        count+=1
print(count)