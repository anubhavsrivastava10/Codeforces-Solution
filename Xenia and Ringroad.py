n,m = map(int,input().split())
lst = list(map(int,input().split()))
c=lst[0]-1
for i in range(1,m):
    if lst[i]<lst[i-1]:
        c+=(n-lst[i-1])
        c+=lst[i]
    else:
        c+=lst[i]-lst[i-1]
    # print(c)
print(c)