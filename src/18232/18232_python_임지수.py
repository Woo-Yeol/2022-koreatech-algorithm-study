import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())    # N : 점 개수, M : 텔레포트 정거장 개수
S, E = map(int, input().split())    # S : 현위치, E : 목적지

teleportGates = defaultdict(deque)

for _ in range(M):
    g1, g2 = map(int, input().split())
    teleportGates[g1].append(g2)
    teleportGates[g2].append(g1)    # 양방향 이동 고려

load = [False for _ in range(1, N+2)]   # 인덱스 0 제외하고 생각할 것
q = deque([(S, 0)])     # S에서 출발(cnt = 0)
load[S] = True

while q:
    st, cnt = q.popleft()
    if st == E:
        break
    if 0 < st+1 <= N and not load[st+1]:
        load[st+1] = True
        q.append((st+1, cnt+1))
    if 0 < st-1 <= N and not load[st-1]:
        load[st-1] = True
        q.append((st-1, cnt+1))
    if st in teleportGates:
        for dt in teleportGates[st]:
            if not load[dt]:
                load[dt] = True
                q.append((dt, cnt+1))

print(cnt)
