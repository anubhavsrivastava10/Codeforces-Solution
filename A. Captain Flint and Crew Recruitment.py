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
    n = ip()

    if(n<31):
        print("NO")
    else:
        print("YES")
        if(n==36):
            print(5,6,10,15)
        elif(n==40):
            print(6,5,14,15)
        elif(n==44):
            print(6,7,10,21)
        else:
            print(6,10,14,n-30)