arr = list(map(int,input().split()))
arr.sort()
val = arr[0]+arr[1]
val2 = arr[1]+arr[2]
if val>arr[2]:
    print('TRIANGLE')
else:
    if val2>arr[3]:
        print('TRIANGLE')
    elif val==arr[2] or val2==arr[3]:
        print('SEGMENT')
    else:
        print('IMPOSSIBLE')