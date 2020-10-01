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

t = ip()
while t:
    t-=1
    n,m = mip()
    arr = matip(n,m)
    row = col = 0
    for i in range(n):
        if arr[i].count(0)==m:
            row+=1
    for i in range(m):
        p = 0
        for j in range(n):
            if arr[j][i]==0:
                p+=1
        if p==n:
            col+=1
    if min(row,col)%2==0:
        print('Vivek')
    else:
        print('Ashish')