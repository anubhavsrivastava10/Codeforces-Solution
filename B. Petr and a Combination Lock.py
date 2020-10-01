arr = [0]
t = int(input())
while t:
    t-=1
    n = int(input())
    lst = []
    for i in arr:
        lst.append(n+i)
        lst.append(n-i)
    arr = lst
for i in arr:
    if i%360==0:
        print("YES")
        break
else:
    print("NO")