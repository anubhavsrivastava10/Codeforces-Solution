n,m = map(int,input().split())
lst = list(map(int,input().split()))
lst = sorted(lst)
c=0
for i in range(m):
    if lst[i]<=0:
        c+=abs(lst[i])
    else:
        break
print(c)