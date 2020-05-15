x = input()
upper=0
lower=0
for i in x:
    if i.islower()==True:
        lower+=1
    else:
        upper+=1
if lower>=upper:
    print(x.lower())
else:
    print(x.upper())