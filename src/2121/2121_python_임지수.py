import sys

N = int(input())
garo, sero = map(int, input().split())
# points = [tuple(map(int, input().split())) for _ in range(N)]
points = set(tuple(map(int, input().split())) for _ in range(N))
result = 0

for (x, y) in points:  
    if not (x+garo, y) in points: continue
    if not (x, y+sero) in points: continue
    if not (x+garo, y+sero) in points: continue
    result += 1

# 원하는 직사각형 형성 조건:
# (x, y), (x+garo, y), (x, y+sero), (x+garo, y+sero)
    
print(result)
