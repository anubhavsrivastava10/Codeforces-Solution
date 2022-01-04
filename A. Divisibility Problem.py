t = int(input())
while t:
    t -= 1
    a,b = map(int, input().split())
    if(a%b==0):
        print(0)
    else:
        p = a//b
        q = (p+1)*b
        print(q-a)
