x = int(input())
lst = list(map(int,input().split()))
z = int(input())
k = list(map(int,input().split()))
arr = [0]*(x+1)
for i in range(x):
    arr[lst[i]]+=i+1
q=0
w=0
#print(arr)
for i in k:
    q+=arr[i]
    w+=(x-arr[i]+1)
print(q,w)