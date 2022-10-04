import sys
from collections import deque

N,K = map(int,sys.stdin.readline().split())
que, result = deque([]), []
for i in range(N):
    que.append(str(i+1))

for i in range(N):
    que.rotate(-(K-1))
    result.append(que.popleft())
    
print("<" + ', '.join(result)+ ">")