a,b,c = map(int,input().split())
k=0
s1= ((a*b)//c)**0.5
s2= ((a*c)//b)**0.5
s3= ((c*b)//a)**0.5
k = s1+s2+s3
print(int(k*4))