'''
baekjoon g4 떡장수와 호랑이
https://www.acmicpc.net/problem/16432
'''

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
result = []

def dfs(day, given):
    global result
    if len(result) != 0:
        return
    elif len(given) < N:
        for i in range(len(ricecake_list[day])):
            if day == 0 or visited[day][i] == 0 and ricecake_list[day][i] != given[-1]:
                visited[day][i] = 1
                dfs(day+1, given+[ricecake_list[day][i]])
    else:
        result = given


N = int(input())
ricecake_list = []
visited = []
for i in range(N):
    ricecake_list.append(list(map(int, input()[2:].split())))
    visited.append([0] * len(ricecake_list[i]))

dfs(0, [])
if result:
    for i in result:
        print(i)
else:
    print(-1)
