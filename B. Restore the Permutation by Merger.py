def lp():
    return list(map(int,input().split()))
def ip():
    return int(input())

n = ip()
while n:
    n-=1
    z = int(input())
    lst = list(map(int,input().split()))
    arr = []
    for i in lst:
        if i in arr:
            pass
        else:
            arr.append(i)
        if len(arr)==z:
            break
    print(*arr)