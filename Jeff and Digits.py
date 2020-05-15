x = int(input())
l = list(map(int,input().split()))
l = sorted(l)[::-1]
# print(l)
s=''
if l[-1]==0:
    while(l!=[]):
        sum1 = sum(l)
        if sum1%9==0:
            for i in range(len(l)):
                s+=str(l[i])
            if s[0]=='0':
                print(0)
            else:
                print(s)
            break
        else:
            l = l[1:]
else:
    print(-1)