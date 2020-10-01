s = input()
alpha = [0]*27
for item in s:
    alpha[ord(item) - ord('a')]+=1
odd = 0
for i in alpha:
    if i!=0:
        if i%2!=0:
            odd+=1
if odd == 0 or odd==1:
    print('First')
elif odd%2==0:
    print('Second')
else:
    print('First')