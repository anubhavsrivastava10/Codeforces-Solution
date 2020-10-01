n = int(input())
arr = list(map(int,input().split()))
lst = [0]*n
# print(lst)
for i in range(n):
    lst[arr[i]-1] = i+1
print(*lst)