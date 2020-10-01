def iip():
    return int(input())

def sip():
    return input()

def mip():
    return map(int,input().split())

def lip():
    return list(map(int,input().split()))

t = iip()
p = lip()
n = lip()
lst = [0]*(t+1)
for i in range(1,len(p)):
    lst[p[i]]+=1
for i in range(1,len(n)):
    lst[n[i]]+=1
flag = 0
for i in range(1,t+1):
    if lst[i]==0:
        flag = 1
        break
if flag == 0:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')