x = int(input())
x+=1
while(True):
    x = str(x)
    if len(set(x))==len(x):
        print(int(x))
        break
    else:
        x = int(x)
        x+=1