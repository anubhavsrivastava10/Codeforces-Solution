t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    even = []
    odd = []
    arr = list(map(int, input().split()))
 
    for i in range(len(arr)):
        if arr[i] % 2:
            odd.append(i+1)
        else:
            even.append(i+1)
 
    for i in range(n-1):
        if len(odd) > 1:
            print(odd.pop(), odd.pop())
        else:
            print(even.pop(), even.pop())