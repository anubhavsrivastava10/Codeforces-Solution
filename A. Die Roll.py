a, b = map(int,input().split())
z = max(a,b)
z = 6-z+1
if z%2==0 and z!=6:
    z = z//2
    print(str(z)+'/3')
elif z%3==0 and z!=6:
    print('1/2')
elif z==6:
    print('1/1')
elif z==5:
    print('5/6')
elif z==1:
    print('1/6')