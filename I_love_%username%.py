x = int(input())
lst = list(map(int,input().split()))
less = lst[0]
big = lst[0]
c=0
for i in range(1,x):
    k = lst[i]
    if k<less:
        c+=1
        less = k
    if k>big:
        c+=1
        big = k
print(c)