'''
baekjoon s2 팰린드롬 만들기
https://www.acmicpc.net/problem/1254
2초, 문자열 길이 최대 50
'''

import sys

input = sys.stdin.readline
S = input().rstrip()
result = len(S)

while True:
    if result % 2 == 0:
        compare_length = len(S[result//2:])
        first = S[:result//2][::-1][:compare_length]
        second = S[result//2:]
    else:
        compare_length = len(S[result//2+1:])
        first = S[:result//2][::-1][:compare_length]
        second = S[result//2+1:]
    if first == second:
        break
    result += 1
print(result)