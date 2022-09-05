import sys
roop_count = 1
while(1):
    L, P, V = map(int,sys.stdin.readline().split())
    if(L<P<V):
        a = L*(V//P)
        b = (L)if(V%P>=L)else(V%P)
        print("Case %d: %d" %(roop_count, a + b))
        roop_count += 1
    else:
        break