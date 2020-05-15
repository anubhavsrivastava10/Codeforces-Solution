n = int(input())
if n%2!=0:
    print(-1)
else:
    i=0
    k=2
    z=1
    for i in range(n//2):
        print(i+k,i+z,end=" ")
        k+=1
        z+=1