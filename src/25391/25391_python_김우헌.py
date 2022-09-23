'''
baekjoon s1 특별상
https://www.acmicpc.net/problem/25391
'''

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
scores = []
result = []
for i in range(N):
    scores.append(list(map(int, input().split())))
scores.sort(key=lambda x : x[1], reverse=True)
result += scores[:K]
scores = scores[K:]
scores.sort(key=lambda x: x[0], reverse=True)
result += scores[:M]
print(sum([score[0] for score in result]))


