t = int(input())
while t:
    t-=1
    n = int(input())
    arr = list(map(int,input().split()))
    k = 0
    while(k<n and arr[k]==1):
        k+=1
    if (k%2) ^ (k==n):
        print('Second')
    else:
        print('First')