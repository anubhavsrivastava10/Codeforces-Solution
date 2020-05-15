k = int(input())
lst = list(map(int,input().split()))
lst = sorted(lst)[::-1]
p=0
c=0
for item in lst:
    if p<k:
        p+=item
        c+=1
if p<k:
    print(-1)
else:
    print(c)