arr = list(map(int,input().split()))
dir = input()
flag = 0
for i in range(arr[0]):
    k = dir[i]
    if k=='W' and arr[3]<arr[1]:
        arr[1]-=1
    elif k=='E' and arr[3]>arr[1]:
        arr[1]+=1
    elif k=='N' and arr[2]<arr[4]:
        arr[2]+=1
    elif k=='S' and arr[2]>arr[4]:
        arr[2]-=1
    if arr[1]==arr[3] and arr[2]==arr[4]:
        print(i+1)
        flag = 1
        break
if flag==0:
    print(-1)