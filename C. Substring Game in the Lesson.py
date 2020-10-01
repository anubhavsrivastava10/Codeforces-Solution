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

s = sip()
lst = []
val = 'z'
for item in s:
    if item<val:
        lst.append(item)
        val = item
    else:
        lst.append(val)

for i in range(len(s)):
    if lst[i]<s[i]:
        print('Ann')
    else:
        print('Mike')