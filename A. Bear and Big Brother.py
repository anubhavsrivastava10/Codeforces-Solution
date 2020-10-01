def iip():
    return int(input())

def sip():
    return input()

def mip():
    return map(int,input().split())

def lip():
    return list(map(int,input().split()))

a,b = mip()
count = 0
while(a<=b):
    a = 3*a
    b = 2*b
    count+=1
print(count)