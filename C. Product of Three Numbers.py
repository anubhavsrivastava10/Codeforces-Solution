t = int(input())
while t:
    t-=1
    n = int(input())
    i = 2
    val = []
    while(i*i<=n):
        if n%i==0:
            n = n//i
            val.append(i)
            break
        i+=1
    i = 2
    while(i*i<=n):
        if n%i==0 and i!=val[0]:
            n = n//i
            val.append(i)
            break
        i+=1
    if len(val)<2 or n==1 or val[-1]==n:
        print('NO')
    else:
        print('YES')
        val.append(n)
        print(*val)