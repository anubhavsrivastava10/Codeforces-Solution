t = int(input())
while t:
    t-=1
    n,k = map(int,input().split())
    i = n-2
    s = ['a']*n
    while i>=0:
        if k<=(n-i-1):
            s[i] = 'b'
            s[n - k] = 'b'
            break
        k -= (n - i - 1)
        i -= 1
    print("".join(s))
"""
https://codeforces.com/blog/entry/75246?#comment-594464
"""