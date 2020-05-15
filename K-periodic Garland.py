# Do the same concept in C++ to remove TLE
for i in range(int(input())):
    n,k=map(int,input().split())
    max1=0
    num = input()
    count=0
    for j in range(n):
        if num[j]=='1':
            count+=1
    for j in range(k):
        c=0
        for p in range(j,n,k):
            if num[p]=='1':
                c+=1
            else:
                c=max(0,c-1)
            max1=max(max1,c)
    print(count-max1)