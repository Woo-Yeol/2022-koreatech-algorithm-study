'''
baekjoon g5 옥상 정원 꾸미기
https://www.acmicpc.net/problem/6198

'''

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
building_height = deque()
result = 0
for i in range(0, N):
    n = int(input())
    while building_height:
        if building_height[-1] <= n:
            building_height.pop()
        else:
            break
    result += len(building_height)
    building_height.append(n)
    print(building_height)
        
print(result)