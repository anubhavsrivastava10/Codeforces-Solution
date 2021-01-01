import sys
from functools import reduce
from collections import Counter
import time
import datetime
import math

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

# def sip(): return sys.stdin.readline()
def sip() : return input()

def mip(): return map(int,sys.stdin.readline().split())

def mips(): return map(str,sys.stdin.readline().split())

def lip(): return list(map(int,sys.stdin.readline().split()))

def matip(n,m):
    lst=[]
    for i in range(n):
        arr = lip()
        lst.insert(i,arr)
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

n,m = mip()
lst = []
for i in range(n):
    s = sip()
    arr = []
    for j in range(m):
        arr.append(s[j])
    lst.append(arr)
# print(lst)
count = 0
if n==1 and m==1:
    print(0)
else:
    for i in range(n):
        for j in range(m):
            if lst[i][j]=='W':
                if j==0 and m>1:
                    if lst[i][j+1]=='P':
                        lst[i][j]='.'
                        lst[i][j+1]='.'
                        count+=1
                elif j==m-1 and m>1:
                    if lst[i][j-1]=='P':
                        lst[i][j]='.'
                        lst[i][j-1]='.'
                        count+=1
                elif m>1:
                    if lst[i][j+1]=='P':
                        lst[i][j]='.'
                        lst[i][j+1]='.'
                        count+=1
                    elif lst[i][j-1]=='P':
                        lst[i][j]='.'
                        lst[i][j-1]='.'
                        count+=1
    for j in range(m):
        for i in range(n):
            if lst[i][j]=='W':
                if i==0 and n>1:
                    if lst[i+1][j]=='P':
                        lst[i][j]='.'
                        lst[i+1][j]='.'
                        count+=1
                elif i==n-1 and n>1:
                    if lst[i-1][j]=='P':
                        lst[i][j]='.'
                        lst[i-1][j]='.'
                        count+=1
                elif n>1:
                    if lst[i-1][j]=='P':
                        lst[i][j]='.'
                        lst[i-1][j]='.'
                        count+=1
                    elif lst[i+1][j]=='P':
                        lst[i][j]='.'
                        lst[i+1][j]='.'
                        count+=1
    print(count)
# print(time.process_time())