x = int(input())
string = sorted(input())
count=0
for i in range(len(string)):
    if i%x==0:
        ch=string[i]
    if string[i]==ch:
        count+=1
if count==len(string) and count%x==0:
    for i in range(x):
        for j in range(0,len(string),x):
            print(string[j],end='')
else:
    print(-1)