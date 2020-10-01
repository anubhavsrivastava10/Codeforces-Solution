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

n,m,x,y = mip()
print(x,y)
for i in range(1,m+1):
    if i!=y:
        print(x,i)
count = 0
p = x
while p>1:
    p-=1
    if count%2==0:
        count+=1
        for i in range(m,0,-1):
            print(p,i)
    else:
        count+=1
        for i in range(1,m+1):
            print(p,i)
p = x
while p<n:
    p+=1
    if count%2==0:
        count+=1
        for i in range(m,0,-1):
            print(p,i)
    else:
        count+=1
        for i in range(1,m+1):
            print(p,i)
    
# count = 0
# p = x-1
# z = y
# while p>0:
#     p -= 1
#     z -= 1
#     if count%2==0:
#         count+=1
#         for i in range(m,0,-1):
#             print(z,i)
#     else:
#         count+=1
#         for i in range(1,m+1):
#             print(z,i)
# p = x+1
# z = y
# while p<n+1:
#     p += 1
#     z += 1
#     if count%2==0:
#         count+=1
#         for i in range(m,0,-1):
#             print(z,i)
#     else:
#         count+=1
#         for i in range(1,m+1):
#             print(z,i)