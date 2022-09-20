'''
baekjoon s2 텔레포트 정거장
https://www.acmicpc.net/problem/18232
'''

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
S, E = map(int, input().split())
teleport_graph = {}
for i in range(M):
    a, b = map(int, input().split())
    if not teleport_graph.get(a):
        teleport_graph[a] = []
    teleport_graph[a].append(b)
    if not teleport_graph.get(b):
        teleport_graph[b] = []
    teleport_graph[b].append(a)

meet_success = False
t = 0
curr_point = S
curr_cycle = deque([S])
next_cycle = deque()
visited_point = set()
while True:
    while curr_cycle:
        curr_point = curr_cycle.popleft()
        if curr_point == E:
            meet_success = True
            break
        if 1 <= curr_point <= N and not curr_point in visited_point:
            next_cycle.append(curr_point+1)
            next_cycle.append(curr_point-1)
            if teleport_graph.get(curr_point):
                for i in teleport_graph[curr_point]:
                    next_cycle.append(i)
        visited_point.add(curr_point)
    if not meet_success and next_cycle:
        t += 1
        curr_cycle = next_cycle
        next_cycle = deque()
        continue
    else:
        break
print(t)