n = int(input())
arr = list(map(int,input().split()))
lst = list(map(int,input().split()))
if sum(arr)>=sum(lst):
    print('Yes')
else:
    print('No')