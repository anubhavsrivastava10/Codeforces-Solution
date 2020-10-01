n, x = map(int, input().split())
arr = set(map(int, input().split()))
flag = 0
if len(arr) < n:
    print(0)
    flag = 1
if flag==0:
    for item in arr:
        if item & x != item and item & x in arr:
            print(1)
            flag = 1
            break
    if flag == 0:
        a = set(aa & x for aa in arr)
        if len(a) < n:
            print(2)
            flag = 1
    if flag==0:
        print(-1)