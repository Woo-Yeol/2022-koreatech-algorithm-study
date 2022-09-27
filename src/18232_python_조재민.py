from collections import deque
from glob import glob
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
S, E = map(int,input().split())
teleport = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    teleport[x].append(y)
    teleport[y].append(x)

def bfs(start):
    q = deque()
    q.append((start, 0))
    while q:
        x, d = q.popleft()
        if x == E:
            return d
        if 1 <= x <= N:
            if not visited[x]:
                visited[x] = True
                q.append((x+1, d+1))
                q.append((x-1, d+1))
                if len(teleport[x]) > 0:
                    for i in teleport[x]:
                        q.append((i, d+1))

print(bfs(S))