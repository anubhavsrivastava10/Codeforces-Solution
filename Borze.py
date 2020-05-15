x = input()
i=0
s=''
while(i<len(x)):
    if x[i]=='.':
        s+='0'
        i+=1
    elif x[i]=='-' and x[i+1]=='-':
        s+='2'
        i+=2
    else:
        s+='1'
        i+=2
print(s)