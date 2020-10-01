def iip():
    return int(input())

def sip():
    return input()

def mip():
    return map(int,input().split())

def lip():
    return list(map(int,input().split()))

t = iip()
s = sip()
a = d = 0
for i in range(t):
    if s[i]=='A':
        a+=1
    else:
        d+=1
if a>d:
    print('Anton')
elif d>a:
    print('Danik')
else:
    print('Friendship')