"""
https://www.acmicpc.net/problem/13702
이상한 술집
"""
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

kettles = [int(input()) for _ in range(N)]

min_volume, max_volume = 1, max(kettles)

res = 0
while min_volume <= max_volume:
    mid = (min_volume + max_volume) // 2
    T_K = sum(kettle // mid for kettle in kettles)
    if T_K >= K:
        res = mid
        min_volume = mid + 1
    else:
        max_volume = mid - 1

print(res)

"""
2 3
702
429

351
"""
