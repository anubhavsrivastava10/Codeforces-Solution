for _ in range(int(input())):
    x = int(input())
    if x%2!=0:
        print((x-1)//2)
    else:
        print((x//2)-1)