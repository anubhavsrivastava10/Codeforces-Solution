for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    pos=[]
    neg=[]
    c=0
    for i in range(n)
        if lst[i]<0:
            neg.append(lst[i])
            if pos!=[]:
                c+=max(pos)
                pos=[]
        if lst[i]>0:
            pos.append(lst[i])
            if neg!=[]:
                c+=max(neg)
                neg=[]
    if pos==[]:
        c+=max(neg)
    else:
        c+=max(pos)
    print(c)