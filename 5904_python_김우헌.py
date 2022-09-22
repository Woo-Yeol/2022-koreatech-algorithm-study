'''
baekjoon g5 Moo게임
https://www.acmicpc.net/problem/5904
'''

import sys

input = sys.stdin.readline
N = int(input())

def moo(length, cur, N):
    prev = (length-cur)//2
    if N <= prev: return moo(prev, cur-1, N)
    elif N > prev+cur: return moo(prev, cur-1, N-prev-cur)
    else: return "o" if N-prev-1 else "m"

length, n = 3, 0
while N > length:
    n += 1
    length = length*2+n+3

print(moo(length, n+3, N))