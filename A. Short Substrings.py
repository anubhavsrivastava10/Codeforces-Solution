t = int(input())
while t:
    t-=1
    n = input()
    k = len(n)
    if k>=2:
        i = 0
        b = ''
        while(i<k):
            b+=n[i]
            i+=2
        b+=n[-1]
        print(b)
    else:
        print(n)