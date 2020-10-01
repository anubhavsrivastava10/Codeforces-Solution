n, m, a = map(int,input().split())
if n%a==0:
    ans = n//a
else:
    ans = (n//a)+1
if m%a==0:
    val = m//a 
else:
    val = (m//a)+1
print(ans*val)