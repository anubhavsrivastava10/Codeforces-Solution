x = input()
x1 = input()
s=""
for i in range(len(x)):
    if x[i]==x1[i]:
        s+='0'
    else:
        s+='1'
print(s)