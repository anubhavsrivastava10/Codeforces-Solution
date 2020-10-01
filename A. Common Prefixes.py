t = int(input())
while t:
    t-=1
    n = int(input())
    arr = list(map(int,input().split()))
    list1 = ['a']*200
    print(('').join(list1))
    for i in arr:
        if  list1[i] == 'a':
            list1[i] = 'b'
            print(('').join(list1))
        else:
            list1[i] = 'a'
            print(('').join(list1))