x = int(input())
lst = list(map(int,input().split()))
z=99999999
k=0
for i in range(x-1):
    p = abs(lst[i]-lst[i+1])
    if p<z:
        z=p
        k=i
if z<abs(lst[-1]-lst[0]):
    print(k+1,k+2)
else:
    print(x,1)
