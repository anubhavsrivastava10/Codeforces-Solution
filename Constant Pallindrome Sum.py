def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        Sum=[0] *( 2 * k +2)
        Sum[0] = n
        m = 0
        for i in range( n/ /2):
            x = a[i ] +a[ n - 1 -i]
            Sum[x]+=-1
            Sum[x+1]+=1
            x=min(a[i],a[n -1-i])+1
            Sum[x]+=-1
            x=max(a[i],a[ n -1-i])+k
            Sum[x+1]+=1
            m=Sum[0]
        for i in range(1, 2*k+2):
            Sum [ i ] +=Sum[i-1]
            m =min(m,Sum[i])
            print(m)

if name=='__main__':
    main()
