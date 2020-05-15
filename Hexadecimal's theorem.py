from math import *
def previousFibonacci(n):
	a = n/((1 + sqrt(5))/2.0)
	return round(a)

n = int(input())
if n==0:
    print(0,0,0)
if n==1:
    print(1,0,0)
if n>1:
    x = previousFibonacci(n)
    p = previousFibonacci(x)
    print(p,x,0)

