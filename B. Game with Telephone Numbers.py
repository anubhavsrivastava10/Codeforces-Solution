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
 
n = ip()
s = sip()
count = 0
for i in range(n-10):
    if s[i]=="8":
        count+=1
if count>(n-11)//2:
    print('YES')
else:
    print('NO')