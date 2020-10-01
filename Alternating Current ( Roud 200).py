string = input()
new = []
for i in range(len(string)):
    if new==[]:
        new.append(string[i])
    else:
        if new==[]:
            new.append(string[i])
        else:
            if new[-1] == string[i]:
                new.pop()
            else:
                new.append(string[i])
if new==[]:
    print('Yes')
else:
    print('No') 