l=[]
ls=[]
n=int(input())
for _ in range(n):
    a,b = map(int,input().split())
    l.append(a)
    ls.append(b)
a0 = l.count(0)
a1 = l.count(1)
b0 = ls.count(0)
b1 = ls.count(1)
c=0
if a0>=a1:
    c+=a1
else:
    c+=a0
if b0>=b1:
    c+=b1
else:
    c+=b0
print(c)