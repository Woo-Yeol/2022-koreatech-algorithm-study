import sys

n = int(sys.stdin.readline())
data= []
for _ in range(n):
    aux = sys.stdin.readline().split()
    data.append( (int(aux[0]), aux[1]) )
data.sort(key=lambda x : x[0])
for str in data:
    print(str[0] , str[1])