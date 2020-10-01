n, l, r = map(int,input().split())
new = n - l +1
small = new
z = 1
for i in range(n-new):
    small += 2**z
    z+=1
z = 0
large = 0
for i in range(n):
    large+= 2**z
    r -= 1
    if r == 0:
        break
    z+=1
for i in range(n-z-1):
    large+=2**z
print(small, large)