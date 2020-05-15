n,k = map(int,input().split())
if n%2!=0:
    l = n//2+1
    if k<=l:
        print((2*k)-1)
    else:
        print(2*(k-l))
else:
    l=n//2
    if k<=l:
        print((2*k)-1)
    else:
        print(2*(k-l))