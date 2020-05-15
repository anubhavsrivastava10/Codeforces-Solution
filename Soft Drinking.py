n,k,l,c,d,salt,nl,np = map(int,input().split())
drink = ((k*l)//n)//nl
lime = (c*d)//n
salt = (salt//n)//np
print(min(drink,salt,lime))