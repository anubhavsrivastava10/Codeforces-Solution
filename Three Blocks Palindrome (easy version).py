from itertools import combinations
for _ in range(int(input())):
    x = int(input())
    lst = list(map(int,input().split()))
    for i in range(1,x+1):
        z = list(combinations(lst,i))

###############  tle for sure
###############  different technique