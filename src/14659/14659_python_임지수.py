import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
q = deque(list(map(int, input().split())))
result = [0]

while len(q) > max(result):     # 종료조건 1 : 남은 봉우리 수가 현재 최대 처치 수 보다 작으면 업데이트 될 가능성 없음
    cnt = 0
    hanzo = q.popleft()
    for bong in q:
        if hanzo > bong:
            cnt += 1
        else:
            break               # 종료조건 2 : 동일 높이 봉우리 없음
    result.append(cnt)
print(max(result))