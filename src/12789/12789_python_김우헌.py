'''
baekjoon s4 도키도키 간식드리미
https://www.acmicpc.net/problem/12789
'''

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
snack_line = deque(map(int, input().split()))
side = deque()
cur_num = 1

while cur_num <= N:
    if len(snack_line) and snack_line[0] == cur_num:
        snack_line.popleft()
        cur_num += 1
        continue
    elif len(side) and side[0] == cur_num:
        side.popleft()
        cur_num += 1
        continue
    elif len(snack_line) and len(side) and snack_line[0] < side[0] or len(side) == 0:
        side.appendleft(snack_line.popleft())
    else:
        break
print(cur_num)
print('Sad') if cur_num <= N else print('Nice')