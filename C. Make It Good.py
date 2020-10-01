n = int(input())
while n:
    n -= 1
    z = int(input())
    count = z - 1
    lst = list(map(int, input().split()))
    while count> 0 and lst[count-1]>=lst[count]:
        count-=1
    while count > 0 and lst[count - 1] <= lst[count]:
        count -= 1
    print(count)