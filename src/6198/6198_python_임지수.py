import sys
from collections import deque


input = sys.stdin.readline

N = int(input())
bulidings = deque([int(input()) for _ in range(N)])
stack = deque()
iCanSee = 0

for buliding in bulidings:
    while stack and stack[-1] <= buliding:
        stack.pop()
    iCanSee += len(stack)
    stack.append(buliding)

print(iCanSee)

