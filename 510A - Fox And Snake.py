n,m = map(int,input().split())
count = 0
for i in range(n):
    if i%2==0:
        print('#'*m)
    elif count%2==0:
        print('.'*(m-1)+'#')
        count+=1
    else:
        print('#'+'.'*(m-1))
        count+=1
