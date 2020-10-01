#incompelte

for i in range(int(input())):
    x = int(input())
    lst=[0]*x
    l=0
    r=x-1
    odd=[]
    evev=[]
    for j in range(1,x+1):
        if j%2==0:
            evev.append(j)
        else:
            odd.append(j)
    for j in range(1,x+1):
        if (r-l+1)%2==0:
            lst[l+r//2]=j
            l=(l+r//2)+1
        print(lst)