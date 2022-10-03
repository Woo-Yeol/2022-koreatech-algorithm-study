'''
baekjoon s2 배열놀이
https://www.acmicpc.net/problem/17123
'''

import sys

input = sys.stdin.readline
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    row_sum, col_sum = [], []
    for i in range(N):
        row_sum.append(sum(matrix[i]))
        col_sum.append(sum([matrix[k][i] for k in range(N)]))
    for i in range(M):
        r1, c1, r2, c2, v = map(int, input().split())
        for i in range(r1-1, r2):
            row_sum[i] += (c2-c1+1)*v
        for i in range(c1-1, c2):
            col_sum[i] += (r2-r1+1)*v

    print(' '.join(list(map(str, row_sum))))
    print(' '.join(list(map(str, col_sum))))