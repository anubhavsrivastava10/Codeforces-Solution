def iip():
    return int(input())

def sip():
    return input()

def mip():
    return map(int,input().split())

def lip():
    return list(map(int,input().split()))

n = iip()
arr = lip()
four = 0
three = 0
two = 0
one = 0
for i in range(n):
    if arr[i] == 4:
        four += 1
    elif arr[i] == 3:
        three += 1
    elif arr[i] == 2:
        two += 1
    else:
        one += 1
taxi = four
taxi += three
if three<one:
    one = one-three
else:
    one = 0
val = one+(2*two)
if val%4==0:
    taxi+= val//4
else:
    taxi += val//4 + 1
print(taxi)