x = int(input())
lst = list(map(int,input().split()))
n = int(input())
ls = list(map(int,input().split()))
k = []
max=0
count=0
for i in ls:
    for j in lst:
        if i%j==0:
            x = i/j
            if x>max:
                max=x
                count = 1
            elif x==max:
                count+=1
print(count)