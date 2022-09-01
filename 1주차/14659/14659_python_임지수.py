from collections import deque
N = int(input())
lst = list(map(int, input().split()))
q = deque(lst)
result = [0]

while len(q) > max(result): # 종료조건 1 : 남은 한조들이 최대 처치 수보다 적으면 갱신될 수 없다.
    cnt = 0
    hanzo = q.popleft()
    for bong in q:
        if hanzo > bong:
            cnt += 1
        else:
            break           # 종료조건 2 : 동일 높이 봉우리 없고, 더 높은 봉우리 만나면 탐색 종료
    result.append(cnt)
print(max(result))

''' 시간초과
from collections import deque
N = int(input())
q = deque(map(int, input().split()))
result = []

while q:
    cnt = 0
    hanzo = q.popleft()
    for bong in q:
        if hanzo > bong:
            cnt += 1
        else:
            break # 동일 높이 봉우리 없음
    result.append(cnt)
print(max(result))
'''

'''
7
6 4 10 2 5 7 11
'''
