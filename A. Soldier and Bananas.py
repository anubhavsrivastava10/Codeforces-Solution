def iip():
    return int(input())

def sip():
    return input()

def mip():
    return map(int,input().split())

def lip():
    return list(map(int,input().split()))

k,n,w = mip()
val = 0
for i in range(w):
    val += k*(i+1)
if val-n>0:
    print(val-n)
else:
    print(0)