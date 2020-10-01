import sys
from functools import reduce
from collections import Counter
import time
import datetime
from math import sqrt,gcd

# def time_t():
#     print("Current date and time: " , datetime.datetime.now())
#     print("Current year: ", datetime.date.today().strftime("%Y"))
#     print("Month of year: ", datetime.date.today().strftime("%B"))
#     print("Week number of the year: ", datetime.date.today().strftime("%W"))
#     print("Weekday of the week: ", datetime.date.today().strftime("%w"))
#     print("Day of year: ", datetime.date.today().strftime("%j"))
#     print("Day of the month : ", datetime.date.today().strftime("%d"))
#     print("Day of week: ", datetime.date.today().strftime("%A"))

def ip(): return int(sys.stdin.readline())

def sip(): return sys.stdin.readline()

def mip(): return map(int,sys.stdin.readline().split())

def mips(): return map(str,sys.stdin.readline().split())

def lip(): return list(map(int,sys.stdin.readline().split()))

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

def check_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**(0.5))+1,2):
        if n%i==0:
            return False
    return True 

# --------------------------------------------------------- #
# sys.stdin = open('input.txt','r')
# sys.stdout = open('output.txt','w')
# --------------------------------------------------------- #

t = ip()
while t:
    t-=1
    n = ip()
    arr = lip()
    zero = 0
    one = 0
    for i in range(n):
        if arr[i]==0:
            zero+=1
        else:
            one+=1
    if zero>=n//2:
        print(zero)
        for i in range(zero):
            print(0,end= ' ')
        print()
    else:
        if one%2==0:
            print(one)
            for i in range(one):
                print(1,end=' ')
        else:
            print(one-1)
            for i in range(one-1):
                print(1,end=' ')
        print()
    
    """Another Slolution for the same"""

    # if n==2:
    #     if arr[0]==arr[1]:
    #         print(2)
    #         print(*arr)
    #     else:
    #         print(1)
    #         print(0)
    # else:
    #     i = 1
    #     lst = []
    #     while i<n:
    #         if arr[i]==arr[i-1]:
    #             lst.append(arr[i])
    #             lst.append(arr[i-1])
    #             i+=2
    #         else:
    #             if i<n-1:
    #                 if arr[i]==arr[i+1]:
    #                     lst.append(arr[i])
    #                     lst.append(arr[i+1])
    #                 else:
    #                     lst.append(arr[i-1])
    #                     lst.append(arr[i+1])
    #                 i+=3
    #             else:
    #                 i+=1
    #     print(len(lst))
    #     print(*lst)