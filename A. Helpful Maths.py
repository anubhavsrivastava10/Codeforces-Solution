string = input()
string = string.split('+')
string.sort()
x = len(string)
for i in range(x):
    if i!=x-1:
        print(string[i],end='+')
    else:
        print(string[i])