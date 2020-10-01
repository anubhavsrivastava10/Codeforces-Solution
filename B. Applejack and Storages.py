from collections import Counter
def ip():
    return int(input())

def sip():
    return input()

def mip():
    return map(int,input().split())


def mips():
	return map(str,input().split())

def lip():
    return list(map(int,input().split()))

def matip(n,m):
    lst=[]
    for i in range(n):
        arr = lip()
        lst.append(arr)
    return lst
 
n = ip()
arr = lip()
count = dict(Counter(arr))
two = 0
four = 0
for i in count.values():
    two += i // 2
    four += i // 4
t = ip()
while t:
    t-=1
    p, s = mips()
    s = int(s)
    if p == "+":
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
        if count[s] % 2 == 0:
            two += 1
        if count[s] % 4 == 0:
            four += 1
    else:
        if count[s] % 2 == 0:
            two -= 1
        if count[s] % 4 == 0:
            four -= 1
        count[s] -= 1
    if two >= 4 and four >= 1:
        print('YES')
    else:
        print("NO")