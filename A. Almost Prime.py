def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    count = []
    for p in range(2, n):
        if prime[p]:
            count.append(p)
    return count

n = int(input())
k = SieveOfEratosthenes(n)
# print(k)
val = 021
for i in range(1,n+1):
    count = 0
    for item in k:
        if item<i:
            if i%item==0:
                count+=1
        else:
            break
    if count==2:
        val+=1
print(val)