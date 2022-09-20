import sys
from collections import deque

def bfs(i, j):
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        for d_x, d_y in zip(dx, dy):
            nx, ny = x+d_x, y+d_y
            if 0 <= nx < N and 0 <= ny < M and lst[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    return 1

input = sys.stdin.readline

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
th = int(input())

lst = [[sum(row[(3*i):(3*i+3)])/3 for i in range(M)] for row in lst] # 각 픽셀별 채널 평균
lst = [[255 if i >= th else 0 for i in row] for row in lst]          # 각 픽셀별 이진화

cnt = 0

visited = [[False for _ in range(M)] for _ in range(N)]
dx = [0, 0, 1, -1] 
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(M):
        if lst[i][j] and not visited[i][j]:
            cnt += bfs(i, j)
   
print(cnt)