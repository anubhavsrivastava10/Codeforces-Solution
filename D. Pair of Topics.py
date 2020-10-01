def binary_search(a,b,l,n):
    mid = l + (l-n) // 2
    if n==0:
        return 0,mid
    if a[mid]<=b[mid]: 
        return 1,mid
    else:
        return binary_search(a,b,l,mid-1)

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort()
z,mid = binary_search(a,b,0,n-1)
if z==1:
    for i in range(mid,n):
        if a[i]<b[i]:
            mid+=1
    ans = mid
    for i in range(mid,n):
        if a[mid]>b[i]:
            ans += 1
    for i in range(n):
        if a[i]>b[i]:
            ans -= 1
        else:
            break
    print(ans)
else:
    print(0)