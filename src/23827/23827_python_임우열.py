"""
https://www.acmicpc.net/problem/23827
수열(Easy)
"""
import sys

input = sys.stdin.readline

N = int(input())
ary = list(map(int, input().split()))

result, term = 0, sum(ary)

for a in ary:
    term -= a
    result += a * term

print(result % (10**9 + 7))
