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

a = sip()
b = sip()
flag = 0
lst = []
if len(a)==len(b):
    for i in range(len(a)):
        if a[i]!=b[i]:
            lst.append(i)
    if len(lst)!=2:
        print('NO')
    else:
        a = list(a)
        b = list(b)
        a[lst[0]],a[lst[1]] = a[lst[1]],a[lst[0]]
        for i in range(len(a)):
            if a[i]!=b[i]:
                flag = 1
        if flag==1:
            print('NO')
        else:
            print('YES')
else:
    print('NO')