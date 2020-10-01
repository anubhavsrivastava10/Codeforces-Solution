t = int(input())
while t:
    t-=1
    present,ans,cnt = 0,0,0
    n,k = map(int,input().split())
    s = input()
    for i in range(n):
        if s[i]=='1':
            if present:
                ans+=max(0,(cnt+1)//(k+1)-1)
            else:
                ans+=cnt//(k+1)
            present=1
            cnt=0
        else:
            cnt+=1
    if present:
        ans+=cnt//(k+1)
    else:
        ans = 1+(n-1)//(k+1)
    print(ans)