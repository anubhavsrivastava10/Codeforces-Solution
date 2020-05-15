x=0
for _ in range(int(input())):
    a,b,c =  map(int,input().split())
    if a==1 and b==1:
        x+=1
    elif a==1 and c==1:
        x+=1
    elif b==1 and c==1:
        x+=1
print(x)