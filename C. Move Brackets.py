t = int(input())
while t:
    t-=1
    a = int(input())
    n = input()
    ans = a//2
    start = []
    count = 0
    for i in range(len(n)):
        if n[i]=='(':
            start.append(n[i])
        elif start==[]:
            count+=1
        else:
            start.pop(-1)
    print(count)