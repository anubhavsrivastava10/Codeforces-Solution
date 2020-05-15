n = int(input())
lst=[]
for _ in range(1):
    a, b = map(int, input().split())
    x = a
    c=a
    x += b
    if c<x:
        c=x
for _ in range(1,n):
    a, b = map(int, input().split())
    x -=a
    x +=b
    if c<x:
        c=x
print(c)