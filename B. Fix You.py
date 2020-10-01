from functools import reduce
def ip():
    return int(input())

def sip():
    return input()

def mip():
    return map(int,input().split())

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

t = ip()
while t:
    t-=1
    n,m = mip()
    arr = []
    for i in range(n):
        s = sip()
        lst=[]
        for j in range(m):
            lst.append(s[j])
        arr.append(lst)
    val = 0
    if n==1:
        for i in range(m-1):
            if arr[0][i]=='D':
                val+=1
    elif m==1:
        for i in range(n-1):
            if arr[i][0]=='R':
                val+=1
    else:
        for i in range(m-1):
            if arr[n-1][i]=='D':
                val+=1
        for i in range(n-1):
            if arr[i][m-1]=='R':
                val+=1
    print(val)