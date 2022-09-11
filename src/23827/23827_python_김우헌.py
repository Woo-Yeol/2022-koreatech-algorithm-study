'''
baekjoon s4 수열(Easy)
https://www.acmicpc.net/problem/23827
'''

import sys

input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().split()))
temp = sum(num_list)
result = 0
for i in range(N-1):
    temp -= num_list[i]
    result += num_list[i] * temp
print(result % 1_000_000_007)