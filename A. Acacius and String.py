# incompelete

t = int(input())
while t:
    t -= 1
    n = int(input())
    str1 = input()
    val = "abacaba"
    j = 0
    for i in range(n):
        if (str1[i]==val[j] or str1[i]=='?') and j<=7:
            j+=1
            if j<=7:
                print(val[j-1],end='')
            elif str1[i]=='?':
                print('d',end='')
            else:
                print(str1[i])
        else:
            j = 0

            print(str1[i])
    print()