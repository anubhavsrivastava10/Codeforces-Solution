def prime(n):
    for val in range(2, int(n ** 0.5) + 1):
        if n % val == 0:
            return False
    return True


t = int(input())
while t:
    t -= 1
    l, r, m = map(int, input().split())
    z = r - l
    c = r
    b = l
    m += z
    a = l
    for i in range(l, r + 1):
        if m % i == 0:
            a = i
            break
    print(a, b, c)
