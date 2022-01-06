q,t = map(int,input().split())
t = 240-t
val = 0
for i in range(1,q+1):
    if t >= 5*i:
        t-=5*i
        val+=1
print(val)
