n = int(input())
arr = list(map(int,input().split()))
val = [0]*1001
for i in range(n):
    val[arr[i]]+=1
print(max(val),len(set(arr)))