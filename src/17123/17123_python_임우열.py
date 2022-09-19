"""
https://www.acmicpc.net/problem/17123
배열 놀이
"""
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    values = [map(int, input().split()) for _ in range(M)]

    row_sum = list()
    col_sum = list()

    for i in range(N):
        row_sum.append(sum(mat[i]))
        col_sum.append(sum(mat[j][i] for j in range(N)))

    # 연산
    for r1, c1, r2, c2, v in values:
        for r in range(r1 - 1, r2):
            row_sum[r] += (c2 - c1 + 1) * v
        for c in range(c1 - 1, c2):
            col_sum[c] += (r2 - r1 + 1) * v

    # 결과 출력
    print(*row_sum)
    print(*col_sum)


# # 전체 과정
# import sys

# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     N, M = map(int, input().split())
#     mat = [list(map(int, input().split())) for _ in range(N)]
#     values = [list(map(int, input().split())) for _ in range(M)]

#     # 연산
#     for r1, c1, r2, c2, v in values:
#         for r in range(r1 - 1, r2):
#             for c in range(c1 - 1, c2):
#                 mat[r][c] += v

#     # 결과 연산
#     results = dict()
#     for row in range(N):
#         row_sum, col_sum = 0, 0
#         for col in range(N):
#             row_sum += mat[row][col]
#             col_sum += mat[col][row]

#         if "r" not in results:
#             results["r"] = [row_sum]
#             results["c"] = [col_sum]
#         else:
#             results["r"].append(row_sum)
#             results["c"].append(col_sum)

#     # 결과 출력
#     for result in results.values():
#         for r in result:
#             print(r, end=" ")
#         print()

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

17 21 21
21 14 24
-30 10
-20 0
2000
2000
"""
