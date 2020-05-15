number = input()
count=0
num=0
flag=0
for i in range(len(number)):
    if number[i]=='0':
        count+=1
        num=0
    if number[i]=='1':
        num+=1
        count=0
    if count==7 or num==7:
        print('YES')
        flag=1
        break
if flag==0:
    print('NO')