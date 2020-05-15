z=k=0
lst = []
for i in range(5):
    ls = list(map(int,input().split()))
    if ls.count(1)==1:
        for j in range(5):
            if ls[j]==1:
                z=j
                k=i
                break
print(abs(z-2)+abs(k-2))