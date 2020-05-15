for _ in range(int(input())):
    x = int(input())
    arr=[0]*(x+1)
    lst = list(map(int,input().split()))
    for item in lst:
        arr[item]+=1
    k = max(arr)
    p = x+1-arr.count(0)
    l1 = min(k-1,p)
    l2 = min(k,p-1)
    print(max(l1,l2))