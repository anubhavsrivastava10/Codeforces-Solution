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

import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
n,m = map(int, sys.stdin.readline().strip().split())
if n>=m:
    for i in range(n+m):
        if i%2==0:
            print('B',end='')
        elif m>0:
            print('G',end='')
            m-=1
        else:
            print('B',end='')
else:
    for i in range(n+m):
        if i%2==0:
            print('G',end='')
        elif n>0:
            print('B',end='')
            n-=1
        else:
            print('G',end='')
