x = int(input())
lst = list(map(int,input().split()))
while(x>0):
    for i in range(7):
        x-=lst[i]
        if x<=0:
            p=i
            break
print(p+1)