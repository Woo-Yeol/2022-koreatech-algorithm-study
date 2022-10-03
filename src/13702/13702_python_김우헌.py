'''
baekjoon s3 이상한 술집
https://www.acmicpc.net/problem/13702
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
pots = []
for i in range(n):
    pots.append(int(input()))
pots.sort(reverse=True)

start = 1
end = max(pots)

while start <= end:
    mid = (start + end) // 2
    temp = sum([pot // mid for pot in pots])
    if temp >= k:
        start = mid + 1
    else:
        end = mid - 1

print(end)