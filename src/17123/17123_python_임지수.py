import sys

input = sys.stdin.readline

T = int(input())                            # number of test cases

for _ in range(T):
    N, M = map(int, input().split())        # number of rows(columns), parameter case
    array = [list(map(int, input().split())) for _ in range(N)]
    
    sumOfRows = [sum(row) for row in array]
    sumOfCols = [sum(col) for col in zip(*array)]

    for _ in range(M):
        r1, c1, r2, c2, v = map(int, input().split())
        for row in range(r1-1, r2):
            sumOfRows[row] += v*(c2-c1+1)       # 각 row 별 포함된 column의 개수만큼 v 증감
        for column in range(c1-1, c2):
            sumOfCols[column] += v*(r2-r1+1)    # 각 column 별 포함된 row의 개수만큼 v 증감
        
    print(*sumOfRows)
    print(*sumOfCols)