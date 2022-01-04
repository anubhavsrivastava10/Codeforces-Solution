n = int(input())
even = (n//2)*((n//2)+1)
if n%2==0:
    odd = (n//2)**2
else:
    odd = ((n//2)+1)**2
print(even - odd)
