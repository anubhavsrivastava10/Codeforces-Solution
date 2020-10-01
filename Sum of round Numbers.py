for i in range(int(input())):
    x = input()[::-1]
    ls=[]
    count=0
    for j in range(len(x)):
        p = x[j]
        if p!='0':
            count+=1
            z = 10**j
            ls.append(int(p)*z)
    print(count)
    print(*ls)