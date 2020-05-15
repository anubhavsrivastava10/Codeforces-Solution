x = int(input())
name = input()
c=0
for i in range(x-1):
    if name[i]==name[i+1]:
        c+=1
print(c)