for i in range(int(input())):
    x = int(input())
    su1=0
    for j in range(x//2):
        p = (x*4)-4
        z = x//2
        k = p*z
        su1 += k
        x-=2
    print(su1)