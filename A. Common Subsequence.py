t = int(input())
while t:
    t-=1
    n,m = map(int,input().split())
    lst = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    op = []
    count = 0
    if n<=m:
        for i in range(n):
            if lst[i] in arr:
                op.append(lst[i])
                count+=1
            if count==1:
                break
    else:
        for i in range(m):
            if arr[i] in lst:
                op.append(arr[i])
                count+=1
            if count==1:
                break
    if op==[]:
        print('NO')
    else:
        print('YES')
        print(count,*op)