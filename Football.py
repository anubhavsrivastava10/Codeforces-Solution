x = int(input())
lst=[]
for i in range(x):
    p = input()
    lst.append(p)
print(max(lst,key=lst.count))
