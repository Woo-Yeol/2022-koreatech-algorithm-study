'''
baekjoon s1 겹치는 건 싫어
https://www.acmicpc.net/problem/20922
'''

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
num_list = list(map(int, input().split()))
max_length = 0
sequence = {}
sequence_start_index = 0

for i in range(len(num_list)):
    if not sequence.get(num_list[i]):
        sequence[num_list[i]] = 0
    if sequence[num_list[i]] == K: # 수열 조정
        max_length = max(max_length, sum(sequence.values()))
        while sequence[num_list[i]] == K:
            sequence[num_list[sequence_start_index]] -= 1
            sequence_start_index += 1
    sequence[num_list[i]] += 1


max_length = max(max_length, sum(sequence.values()))
print(max_length)
