import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
order = deque(map(int, input().split()))    # order는 스택으로 활용
extra = deque([])                           # extra는 큐로 활용
cnt = 1

while order:
    if order[0] == cnt:                     # order와 extra의 처음 원소를 peek
        order.popleft()                     # cnt와 맞으면 cnt 증가 후 내보내기
        cnt += 1
        continue
    if extra and extra[-1] == cnt:      
        extra.pop()
        cnt += 1
        continue

    extra.append(order.popleft())           # 둘 다 아니면 extra에 적재

while extra:                                # 남은 extra 처리
    current = extra.pop()                   # 다시 역방향으로 옮길 수 없으니 계속 pop했을 때 순서가 맞아야 함
    if current == cnt:
        cnt += 1
    else:
        break

print("Nice") if cnt == N+1 else print("Sad")
