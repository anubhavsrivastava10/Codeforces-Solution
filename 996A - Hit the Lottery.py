n = int(input())
lst = [100,20,10,5,1]
count = 0
for item in lst:
    if n>=item:
        count += n//item
        n = n- (n//item)*item
print(count)
