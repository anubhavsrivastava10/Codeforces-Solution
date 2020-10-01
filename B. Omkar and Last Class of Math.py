import math

t = int(input())
while t:
    t -= 1
    n = int(input())
    k = int(math.sqrt(n)) + 1
    # print(k)
    i = 2
    s = -1
    while i <= k:
        if n % i == 0:
            n = n // i
            break
        i += 1
    if s == -1:
        print(1, n - 1)
    else:
        print(s, n - s)
