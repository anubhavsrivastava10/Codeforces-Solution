a,b = map(int,input().split())
for i in range(a):
    string = input()
    for j in range(len(string)):
        if string[j]!='-':
            if i%2==0 and j%2==0:
                print('W', end="")
            if i%2==0 and j%2!=0:
                print('B', end="")
            if i%2!=0 and j%2==0:
                print('B', end="")
            if i%2!=0 and j%2!=0:
                print('W', end="")
        else:
            print('-', end="")
    print()