x = 0
for _ in range(int(input())):
    z = input()
    if z[0]=='+' or z[-1]=='+':
        x+=1
    else:
        x-=1
print(x)