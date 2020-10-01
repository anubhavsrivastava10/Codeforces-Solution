x = list(input())
lst = list(map(int, input().split()))
maxx = max(lst)
minn = min(lst)
max_count = lst.count(maxx)
min_count = lst.count(minn)
if maxx == minn:
    print(maxx - minn, max_count * (max_count - 1) // 2)
else:
    print(maxx - minn, max_count * min_count)
