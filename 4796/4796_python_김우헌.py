'''
baekjoon b1 캠핑
https://www.acmicpc.net/problem/4796
'''

import sys
import math

input = sys.stdin.readline
i = 1
while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    print(f"Case {i}: {V // P * L + eval('L if V % P >= L else V % P')}")
    i += 1
