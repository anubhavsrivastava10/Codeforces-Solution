from collections import Counter
n = int(input())
arr = [ input() for i in range(n) ]
a = Counter()
b = []
for i in range(n):
  nm, s = arr[i].split()
  a[nm] += int(s)
  b.append((nm, a[nm]))
mx = max(a.values())
print([nm for (nm, s) in b if s >= mx and a[nm] == mx][0])