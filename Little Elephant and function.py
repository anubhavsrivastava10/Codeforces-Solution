def fun(x):
    print(x,end=" ")
    for i in range(1,x):
        print(i,end=" ")
x = int(input())
if x>1:
    fun(x)
else:
    print(1)