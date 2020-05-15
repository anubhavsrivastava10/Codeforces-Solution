for _ in range(int(input())):
    x = int(input())
    lst = list(map(int,input().split()))
    ls = list(map(int,input().split()))
    lst = sorted(lst)[::-1]
    ls = sorted(ls)[::-1]
    c=0
    j=0
    for i in range(x):
        while(j<x):
            if lst[i]>ls[j]:
                c+=1
                j+=1
                break
            else:
                j+=1
    print(c)