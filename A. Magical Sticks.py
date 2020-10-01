t = int(input())
while t:
    t-=1
    n = int(input())
    if n<3:
        print(1)
    elif n==3 or n==4:
        print(2)
    else:
        if n%2==0:
            print(n//2)
        else:
            print((n//2)+1)