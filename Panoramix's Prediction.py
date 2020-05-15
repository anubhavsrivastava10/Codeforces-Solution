def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

k=0
n,m = map(int,input().split())
if isprime(m)==True:
    for i in range(n+1,m+1):
        if isprime(i)==True:
            k=i
            break
        else:
            k=0
    if k == m:
        print('YES')
    else:
        print('NO')
else:
    print('NO')