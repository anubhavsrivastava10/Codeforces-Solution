n = int(input())
arr = list(map(int,input().split()))
even = 0
odd = 0
flag = 0
for i in range(n):
    if arr[i]%2==0:
        even += 1
        eve = i
    else:
        odd += 1
        od = i
if even<odd:
    print(eve+1)
else:
    print(od+1)