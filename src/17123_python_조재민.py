# 배열 놀이
# https://www.acmicpc.net/problem/17123

import sys
input = sys.stdin.readline
Test_Case = int(input())

for _ in range(Test_Case):
    N, M = map(int,input().split())
    Num_data = []
    row_sum, col_sum = [0]*N, [0]*N

    for _ in range(N):
        Num_data.append(list(map(int,input().split())))

    #행과 열 합을 미리 계산
    for i in range(N):
        for j in range(N):
            row_sum[i] += Num_data[i][j]
            col_sum[j] += Num_data[i][j]

    #시간을 줄이기 위해 행과 열 합의 변동값만 계산
    for _ in range(M):
        r1, c1, r2, c2, v = map(int,input().split())
        for i in range(r1 -1, r2):
            row_sum[i] += (c2 - (c1-1)) * v
        for i in range(c1 -1, c2):
            col_sum[i] += (r2 - (r1-1)) * v
            
    print(" ".join(map(str,row_sum)))
    print(" ".join(map(str,col_sum)))

"""
3
3 3
1 2 3
4 5 6
7 8 9
1 1 2 3 3
2 2 3 2 -5
1 1 3 2 1
2 1
10 20
30 40
1 1 2 2 -30
1 3
1000
1 1 1 1 1000
1 1 1 1 -1000
1 1 1 1 1000

>>
17 21 21
21 14 24
-30 10
-20 0
2000
2000
"""