n,m = map(int,input().split())
c=0
for i in range(n+1):
    for j in range(m+1):
        if i**2+j==n and i+j**2==m:
            c+=1
print(c)