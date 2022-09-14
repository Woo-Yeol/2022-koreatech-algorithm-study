import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
D = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            D[i] = max(D[i], D[j]+1)

print(max(D))