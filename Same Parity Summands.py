# incompelete

for i in range(int(input())):
    a = int(input())
    odd=[]
    even=[]
    if a==2 or a==3:
        print(-1)
    elif a==4:
        print('1 3 2 4')
    else:
        for j in range(1,a+1):
            if j%2==0:
                even.append(j)
            else:
                odd.append(j)
        if a%2==0:
            odd.append(even[-3])
            odd.append(even[-1])
            odd.append(even[-2])
            odd.extend(even[:-3])
            print(*odd)
        else:
            odd.append(even[-2])
            odd.append(even[-1])
            odd.extend(even[:-2][::-1])
            print(*odd)