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
lst = lip()
count = 0
arr = [0]*(max(lst)+1)
for i in range(n):
    arr[lst[i]]+=1
flag = 0
for item in arr:
    if item!=0:
        if item%2==1:
            flag = 1
if flag == 1:
    print('Conan')
else:
    print('Agasa')