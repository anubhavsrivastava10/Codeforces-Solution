for _ in range(int(input())):
    n,a,b = map(int,input().split())
    s=''
    for i in range(n):
        x = 97+(i%b)
        s+=chr(x)
    print(s)