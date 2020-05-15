n = int(input())
lst = list(map(int,input().split()))
a=0
b=100
max_ind=0
min_ind=0
"""
leftmost soldier with the maximum height - 1 + n - number of rightmost soldier with the minimum height
"""
for i in range(n):
    if lst[i]>a:
        a=lst[i]
        max_ind = i
    if lst[i]<=b:
        b = lst[i]
        min_ind = i
if max_ind<min_ind:
    print(max_ind+(n-min_ind)-1)
else:
    print(max_ind+((n-min_ind)-2))