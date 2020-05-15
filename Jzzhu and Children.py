n,m = map(int,input().split())
lst = list(map(int,input().split()))
for i in range(n):
    if lst[i]%m==0:
        lst[i] = lst[i]//m
    else:
        lst[i] = (lst[i]//m)+1
#print(lst)
k = max(lst)
p = lst.index(k)
for i in range(p+1,n):
    if lst[i]==k:
        p=i
print(p+1)