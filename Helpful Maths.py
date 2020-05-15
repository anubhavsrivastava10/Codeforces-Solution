n = input()
x = list(n)
z=[]
for item in x:
    if item!='+':
        z.append(int(item))
z=sorted(z)
l = len(z)
if l>1:
    for i in range(l):
        if i!=l-1:
            print(z[i],end="+")
        else:
            print(z[i])
else:
    print(z[0])