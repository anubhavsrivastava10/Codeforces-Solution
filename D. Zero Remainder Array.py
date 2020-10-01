t = int(input())
while t:
    t-=1
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    a = dict()
    max_value = 0
    flag = 0
    for x in nums:
        if x % k != 0:
            x = k - (x % k)
            if not(x in a.keys()):
                a[x] = x
            else:
                a[x] += k
                x = a[x]
            max_value = max(max_value, x)
            flag = 1
    if flag == 0:
        print(0)
    else:
        print(max_value + 1)