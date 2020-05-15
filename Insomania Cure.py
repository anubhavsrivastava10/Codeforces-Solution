k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
c=d
if(k == 1 or l == 1 or m == 1 or n == 1):
    print(c)
else:
    for i in range(1,d+1):
        if((i%k != 0) and (i%l != 0) and (i%m != 0) and (i%n != 0)):
            c-=1
    print(c)

# i wanted to take out the lcm and do this problem
# but was giving wrong answer