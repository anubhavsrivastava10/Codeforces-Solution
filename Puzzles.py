n,m = map(int,input().split())
lst = sorted(list(map(int,input().split())))
su1=lst[n-1]-lst[0]
for i in range(1,m-n+1):
    if lst[i+n-1]-lst[i]<su1:
        su1 = lst[i+n-1]-lst[i]
print(su1)