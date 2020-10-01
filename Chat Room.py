x = input()
hello = "hello"
j=0
count=0
for i in range(len(x)):
    if x[i]==hello[j]:
        j+=1
        count+=1
    if count==5:
        break
if count==5:
    print("YES")
else:
    print("NO")