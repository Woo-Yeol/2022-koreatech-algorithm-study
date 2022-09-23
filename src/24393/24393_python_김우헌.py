'''
baekjoon s3 조커 찾기
https://www.acmicpc.net/problem/24393
'''

import sys

input = sys.stdin.readline

N = int(input())
cards = [i for i in range(27)]
joker = 0
for i in range(N):
    shuffle_sequence = list(map(int, input().split()))
    left = cards[:13]
    right = cards[13:]
    new_cards = []
    for k in range(len(shuffle_sequence)):
        if k % 2 == 0:
            new_cards += right[:shuffle_sequence[k]]
            right = right[shuffle_sequence[k]:]
        else:
            new_cards += left[:shuffle_sequence[k]]
            left = left[shuffle_sequence[k]:]
    cards = new_cards.copy()
print(cards.index(0)+1)

