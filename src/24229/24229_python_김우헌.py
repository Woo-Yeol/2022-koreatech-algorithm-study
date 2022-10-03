'''
baekjoon g4 모두싸인 출근길
https://www.acmicpc.net/problem/24229
'''
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
data = []
for i in range(N):
    L, R = map(int, input().split())
    data.append([L, R])
data.sort(key = lambda x : x[0])

loads = [data[0]]
for i in data[1:]:
    load = loads[-1]
    if load[1] >= i[0]:
        loads.pop()
        loads.append([load[0], max(i[1], load[1])])
    else:
        loads.append(i)

start, end = 0, 0
max_length = 0
q = deque([0])
visited = set()

while q:
    i = q.popleft()
    if i in visited:
        continue
    else:
        visited.add(i)
    start, end = loads[i]
    jump_power = end - start
    for k in range(i+1, len(loads)):
        if loads[k][0] - end <= jump_power: # k번째 판자로 점프할 수 있다면
            q.append(k)
        else:
            break
    max_length = max(max_length, end)
print(max_length)

