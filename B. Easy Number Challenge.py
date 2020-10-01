from functools import reduce
from collections import Counter
import time
import datetime

def time_t():
    print("Current date and time: " , datetime.datetime.now())
    print("Current year: ", datetime.date.today().strftime("%Y"))
    print("Month of year: ", datetime.date.today().strftime("%B"))
    print("Week number of the year: ", datetime.date.today().strftime("%W"))
    print("Weekday of the week: ", datetime.date.today().strftime("%w"))
    print("Day of year: ", datetime.date.today().strftime("%j"))
    print("Day of the month : ", datetime.date.today().strftime("%d"))
    print("Day of week: ", datetime.date.today().strftime("%A"))

def ip():
    return int(input())

def sip():
    return input()

def mip():
    return map(int,input().split())

def mips():
    return map(str,input().split())

def lip():
    return list(map(int,input().split()))

def matip(n,m):
    lst=[]
    for i in range(n):
        arr = lip()
        lst.append(arr)
    return lst

def factors(n): # find the factors of a number
    return list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def minJumps(arr, n): #to reach from 0 to n-1 in the array in minimum steps
    jumps = [0 for i in range(n)]
    if (n == 0) or (arr[0] == 0):
        return float('inf')
    jumps[0] = 0
    for i in range(1, n):
        jumps[i] = float('inf')
        for j in range(i):
            if (i <= j + arr[j]) and (jumps[j] != float('inf')):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    return jumps[n-1]

def dic(arr): # converting list into dict of count
    return Counter(arr)

def prime(n):
    for i in range(3,int(n**(0.5))+1):
        if n%i==0:
            return False
    return True 

primes = []
for i in range(2,101):
    if prime(i):
        primes.append(i)

a,b,c = mip()
count = 0
if a==1 and b==1 and c==1:
    print(1)
else:
    for i in range(1,a+1):
        for j in range(1,b+1):
            for k in range(1,c+1):
                q = i*j*k
                ans = 1
                for item in primes:
                    if q<item:
                        break
                    y = 1
                    while q%item==0 and q>=1:
                        q = q//item
                        y+=1
                    ans = ans*y
                count += ans
    print(count)
    