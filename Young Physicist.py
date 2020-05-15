a=b=c=0
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    a+=x
    b+=y
    c+=z
if a==b==c==0:
    print('YES')
else:
    print('NO')