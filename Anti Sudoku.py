for _ in range(int(input())):
    for i in range(9):
        ls=list(input())
        s=''
        for j in range(9):
            if ls[j]=='9':
                ls[j]='1'
                s+=ls[j]
            else:
                s+=ls[j]
        print(s)