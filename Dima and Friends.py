x = int(input())
lst = list(map(int,input().split()))
k = sum(lst)
c=0
for i in range(1,6):
    if (k+i)%(x+1)!=1:
        c+=1
print(c)