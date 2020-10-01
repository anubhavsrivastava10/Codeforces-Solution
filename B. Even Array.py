t = int(input())
while t:
    t-=1
    n = int(input())
    arr = list(map(int,input().split()))
    odd = 0
    even = 0
    for i in range(n):
        if i%2!=arr[i]%2:
            if i%2==0:
                even+=1
            else:
                odd+=1
    if even==odd:
        print(even)
    else:
        print(-1)