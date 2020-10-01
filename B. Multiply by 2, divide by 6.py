t = int(input())
while t:
    t-=1
    n = int(input())
    if n == 1:
        print(0)
    else:
        count = 0
        flag = 0
        while flag==0:
            if n%6==0:
                count+=1
                n = n//6
            elif n%6==3:
                count+=1
                n = n*2
            else:
                if n==1:
                    print(count)
                elif n==3:
                    print(count+2)
                else:
                    print(-1)
                flag = 1