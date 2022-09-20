"""
https://www.acmicpc.net/problem/11568
민균이의 계략
"""
import sys

input = sys.stdin.readline

N = int(input())
ary = list(map(int, input().split()))

length = [1 for _ in range(N)]

# https://chanhuiseok.github.io/posts/algo-49/
# 일반적으로 최장 증가 부분 수열의 길이가 얼마인지 푸는 간편한 방법은 DP를 이용
for j in range(N):
    for i in range(j):
        if ary[i] < ary[j]:
            length[j] = max(length[j], length[i] + 1)

print(max(length))
"""
5
8 9 1 2 10

3
"""
