'''
baekjoon s2 민균이의 계략
https://www.acmicpc.net/problem/11568

'''

import sys
import bisect

input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
seq = [cards[0]]
for i in range(1, N):
    if cards[i] > seq[-1]:
        seq.append(cards[i])
    else:
        seq[bisect.bisect_left(seq,cards[i])] = cards[i]
print(len(seq))
    

