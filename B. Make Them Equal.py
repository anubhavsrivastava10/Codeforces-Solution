n = int(input())
arr = list(map(int,input().split()))
new = sorted(set(arr))
k = len(new)
if k>3:
    print(-1)
elif k==1:
    print(0)
elif k == 2:
    if (new[1]-new[0])%2==0:
        print((new[1]-new[0])//2)
    else:
        print(new[1]-new[0])
else:
    if new[1]-new[0]==new[2]-new[1]:
        print(new[1]-new[0])
    else:
        print(-1)