'''
baekjoon s2 영상처리
https://www.acmicpc.net/problem/21938
1초, matrix 사이즈 최대 1000^2
새 화면 만들기 -> O(n)
화면 내 물체 탐색 -> DFS O(n^2)
'''

import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
matrix = []
for i in range(N):
    matrix.append(deque(list(map(int, input().split()))))
T = int(input())

new_matrix = []
for col in matrix:
    row = []
    while col:
        new_pixel = 255 if (col.popleft() + col.popleft() + col.popleft()) / 3 >= T else 0
        row.append(new_pixel)
    new_matrix.append(row)

visited = [[0 for i in range(M)] for j in range(N)]
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

def dfs(x, y):
    visited[y][x] = 1
    for i in range(4):
        next_x = x+dx[i]
        next_y = y+dy[i]
        if 0 <= next_x < M and 0 <= next_y < N \
            and visited[next_y][next_x] == 0 \
            and new_matrix[next_y][next_x] == 255:
            dfs(next_x, next_y)
    
result = 0
for y in range(N):
    for x in range(M):
        if visited[y][x] == 0 and new_matrix[y][x] == 255:
            result += 1
            dfs(x, y)

print(result)
