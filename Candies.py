for _ in range(int(input())):
    x = int(input())
    y = 3
    n=2
    while(x%y!=0):
        z = 2**n
        y+=z
        n+=1
    print(x//y) 