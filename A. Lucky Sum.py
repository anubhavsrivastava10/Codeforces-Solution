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

def get_all_lucky(length):
    if length==1:
        return ['4','7']
    ans=get_all_lucky(length-1)
    temp=ans.copy()
    for i in temp:
        ans.append('4'+i)
        ans.append('7'+i)
    return ans
 
l,r=map(int, input().split())
lucky_nums=get_all_lucky(10)
lucky_nums=list(map(int, lucky_nums))
lucky_nums.sort()
ans=0
for i in lucky_nums:
    num_to_left=max(min(i,r)-l+1,0)
    ans+=num_to_left*i
    l=max(i+1,l)
    if l>r:
        break
print(ans)

# print(time.process_time())