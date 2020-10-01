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
    s = sip()
    n = len(s)
    maxx = 0
    maxxs = 0
    for i in range(0,10):
        maxxs = max(maxxs, s.count(str(i)))
    for i in range(0,100):
        cnt = 0
        y = str(i)
        if(len(y)==1):
            y = "0"+y
        f = 0
        for j in range(n):
            if(s[j]==y[0]):
                f=1
            elif(s[j]==y[1] and f==1):
                cnt+=1
                f=0
        maxx = max(maxx,cnt)
    print(min(len(s)-2*maxx, len(s)-maxxs))