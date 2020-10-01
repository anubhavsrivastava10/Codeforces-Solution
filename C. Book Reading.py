t = int(input())
while t:
    t-=1
    n,m = map(int,input().split())
    sum1 = []
    for i in range(10):
        sum1.append((m*i)%10)
    k = n//m
    val = (k//10)*sum(sum1)
    for i in range((k%10)+1):
        val+=sum1[i]
    print(val)