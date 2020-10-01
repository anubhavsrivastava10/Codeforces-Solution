a,b=map(int,input().split())
c = list(map(int,input().split()))
c.sort()
m=c[a//2]
n=c[a//2]+b
def check(mid):
    s=0
    for  i in range(a//2,a):
        if mid>c[i]:
            s+=(mid-c[i])
        else:
            break
    return s
while(m<=n):
    mid=(m+n)//2
    if(check(mid)<=b):
        m=mid+1
    else:
        n=mid-1
print(m-1)