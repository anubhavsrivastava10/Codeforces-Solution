n = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse=True)
k = n-1
su = 0
su1= 0
for i in range(1,n+1):
    su = sum(arr[:i])
    su1 = sum(arr[i:])
    if su>su1:
        print(i)
        break