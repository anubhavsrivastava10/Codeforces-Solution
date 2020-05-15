x = int(input())
lst = list(map(int,input().split()))
k=99999999999999
z=0
c=0
for i in range(0,x):
    if lst[i]<k:
        c=0
        z=i
        k=lst[i]
    elif lst[i]==k:
        c=1
if c==0:
    print(z+1)
else:
    print("Still Rozdil")

