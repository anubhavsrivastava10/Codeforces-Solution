x = input().lower()
lst=["a", "o", "y", "e", "u", "i"]
c=0
for i in range(len(x)):
    if x[i] not in lst:
        print('.'+x[i],end='')