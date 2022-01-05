n = input()
if n == '{}':
    print(0)
else:
    n = n[1:]
    n = n[:-1]
    n = n.split(',')
    arr = [0]*26
    for item in n:
        item = item.strip()
        arr[ord(item)-97]+=1
    count = 0
    for item in arr:
        if item!=0:
            count+=1
    print(count)
