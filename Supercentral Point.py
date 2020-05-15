lst=[]
z = int(input())
for _ in range(z):
    ls = list(map(int,input().split()))
    lst.append(ls)
k=0
for i in range(z):
    x = lst[i][0]
    y = lst[i][1]
    l=r=u=d=0
    for j in range(z):
        if x==lst[j][0]:
            if y>lst[j][1]:
                d+=1
            if y<lst[j][1]:
                u+=1
        if y==lst[j][1]:
            if x>lst[j][0]:
                l+=1
            if x<lst[j][0]:
                r+=1
    if d>0 and l>0 and u>0 and r>0:
        k+=1
print(k)