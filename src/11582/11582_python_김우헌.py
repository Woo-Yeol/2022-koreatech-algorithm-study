'''
baekjoon s4 치킨 TOP N
https://www.acmicpc.net/problem/11582
'''

import sys

input = sys.stdin.readline

N = int(input())
chicken_taste_score = list(map(int, input().split()))
k = int(input())
while N > k:
    N //= 2
    devide_length = len(chicken_taste_score) // N
    temp = []
    for i in range(N):
        temp += sorted(chicken_taste_score[i*devide_length : (i+1)*devide_length])
    chicken_taste_score = temp.copy()
print(*chicken_taste_score)