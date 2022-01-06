red, blue = map(int,input().split())
if red>blue:
    if (red-blue)%2==0:
        print(blue,(red-blue)//2)
    else:
        print(blue,(red-blue-1)//2)
elif blue>red:
    if (blue-red)%2==0:
        print(red,(blue-red)//2)
    else:
        print(red,(blue-red-1)//2)
else:
    print(red,0)
