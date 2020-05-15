n = int(input())
lst = list(map(int,input().split()))
x=0
for i in range(n):
    x += (lst[i]/100)
print((x/n)*100)